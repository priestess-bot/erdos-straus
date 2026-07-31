#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

namespace {

struct Stats {
    std::int64_t moduli = 0;
    std::int64_t cyclic_moduli = 0;
    std::int64_t cyclic_components = 0;
    std::int64_t cyclic_nodes = 0;
    std::int64_t dangerous_components = 0;
    std::int64_t direct_radical_miss_cycles = 0;
    std::int64_t multiplier_bridge_miss_cycles = 0;
};

struct CycleWitness {
    int modulus = 0;
    std::vector<int> cycle;
    std::vector<int> support;

    bool empty() const { return modulus == 0; }
};

struct Components {
    std::vector<int> id;
    std::vector<std::vector<int>> members;
    std::vector<char> cyclic;
};

long long extended_gcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1 = 0;
    long long y1 = 0;
    const long long divisor = extended_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return divisor;
}

int inverse_mod(int value, int modulus) {
    long long x = 0;
    long long y = 0;
    if (extended_gcd(value, modulus, x, y) != 1) {
        throw std::runtime_error("inverse requested for a non-unit");
    }
    x %= modulus;
    if (x < 0) {
        x += modulus;
    }
    return static_cast<int>(x);
}

std::vector<int> factor_support(int value, const std::vector<int>& spf) {
    std::vector<int> result;
    while (value > 1) {
        const int prime = spf[value];
        result.push_back(prime);
        while (value % prime == 0) {
            value /= prime;
        }
    }
    return result;
}

std::vector<int> merge_support(
    const std::vector<int>& left,
    const std::vector<int>& right
) {
    std::vector<int> result;
    result.reserve(left.size() + right.size());
    std::set_union(
        left.begin(),
        left.end(),
        right.begin(),
        right.end(),
        std::back_inserter(result)
    );
    return result;
}

std::vector<int> node_support(
    int node,
    int modulus,
    const std::vector<int>& spf
) {
    return merge_support(
        factor_support(node, spf),
        factor_support(modulus - node, spf)
    );
}

class CubeOracle {
public:
    explicit CubeOracle(int modulus)
        : modulus_(modulus), marks_(static_cast<std::size_t>(modulus), 0) {}

    bool hits_minus_one(const std::vector<int>& support) {
        const std::string cache_key = key(support);
        const auto cached = minus_one_cache_.find(cache_key);
        if (cached != minus_one_cache_.end()) {
            return cached->second;
        }
        const bool hit = hits_targets(support, {modulus_ - 1});
        minus_one_cache_.emplace(cache_key, hit);
        return hit;
    }

    bool hits_multiplier_targets(const std::vector<int>& support) {
        int radical = 1;
        for (const int prime : support) {
            radical = static_cast<int>(
                static_cast<long long>(radical) * prime % modulus_
            );
        }
        const int lambda = static_cast<int>(4LL * radical % modulus_);
        const int inverse = inverse_mod(lambda, modulus_);
        return hits_targets(
            support,
            {
                modulus_ - 1,
                (modulus_ - lambda) % modulus_,
                (modulus_ - inverse) % modulus_,
            }
        );
    }

private:
    static std::string key(const std::vector<int>& support) {
        std::string result;
        for (const int prime : support) {
            result += std::to_string(prime);
            result.push_back(',');
        }
        return result;
    }

    bool hits_targets(
        const std::vector<int>& support,
        const std::vector<int>& targets
    ) {
        if (++generation_ == std::numeric_limits<int>::max()) {
            std::fill(marks_.begin(), marks_.end(), 0);
            generation_ = 1;
        }
        std::vector<int> residues{1};
        marks_[1] = generation_;
        const auto target_seen = [&]() {
            return std::any_of(
                targets.begin(),
                targets.end(),
                [&](int target) { return marks_[target] == generation_; }
            );
        };
        if (target_seen()) {
            return true;
        }
        for (const int prime : support) {
            const int inverse = inverse_mod(prime % modulus_, modulus_);
            const std::size_t previous_size = residues.size();
            for (std::size_t index = 0; index < previous_size; ++index) {
                const int residue = residues[index];
                const int positive = static_cast<int>(
                    static_cast<long long>(residue) * prime % modulus_
                );
                const int negative = static_cast<int>(
                    static_cast<long long>(residue) * inverse % modulus_
                );
                if (marks_[positive] != generation_) {
                    marks_[positive] = generation_;
                    residues.push_back(positive);
                }
                if (marks_[negative] != generation_) {
                    marks_[negative] = generation_;
                    residues.push_back(negative);
                }
            }
            if (target_seen()) {
                return true;
            }
        }
        return false;
    }

    int modulus_;
    std::vector<int> marks_;
    int generation_ = 0;
    std::unordered_map<std::string, bool> minus_one_cache_;
};

Components strongly_connected_components(
    const std::vector<std::vector<int>>& adjacency,
    const std::vector<char>& included
) {
    const int maximum_node = static_cast<int>(adjacency.size()) - 1;
    std::vector<std::vector<int>> reverse(adjacency.size());
    std::vector<int> active;
    for (int source = 1; source <= maximum_node; ++source) {
        if (!included[source]) {
            continue;
        }
        active.push_back(source);
        for (const int destination : adjacency[source]) {
            if (included[destination]) {
                reverse[destination].push_back(source);
            }
        }
    }

    std::vector<char> seen(adjacency.size(), false);
    std::vector<int> order;
    for (const int root : active) {
        if (seen[root]) {
            continue;
        }
        std::vector<std::pair<int, std::size_t>> stack;
        seen[root] = true;
        stack.emplace_back(root, 0);
        while (!stack.empty()) {
            const int node = stack.back().first;
            std::size_t& edge_index = stack.back().second;
            while (
                edge_index < adjacency[node].size()
                && !included[adjacency[node][edge_index]]
            ) {
                ++edge_index;
            }
            if (edge_index == adjacency[node].size()) {
                order.push_back(node);
                stack.pop_back();
                continue;
            }
            const int destination = adjacency[node][edge_index++];
            if (!seen[destination]) {
                seen[destination] = true;
                stack.emplace_back(destination, 0);
            }
        }
    }

    std::vector<int> component_id(adjacency.size(), -1);
    std::vector<std::vector<int>> members;
    for (auto iterator = order.rbegin(); iterator != order.rend(); ++iterator) {
        const int root = *iterator;
        if (component_id[root] != -1) {
            continue;
        }
        const int id = static_cast<int>(members.size());
        members.emplace_back();
        std::vector<int> stack{root};
        component_id[root] = id;
        while (!stack.empty()) {
            const int node = stack.back();
            stack.pop_back();
            members.back().push_back(node);
            for (const int destination : reverse[node]) {
                if (component_id[destination] == -1) {
                    component_id[destination] = id;
                    stack.push_back(destination);
                }
            }
        }
        std::sort(members.back().begin(), members.back().end());
    }

    std::vector<char> cyclic(members.size(), false);
    for (std::size_t id = 0; id < members.size(); ++id) {
        if (members[id].size() > 1) {
            cyclic[id] = true;
            continue;
        }
        const int node = members[id][0];
        cyclic[id] = std::find(
            adjacency[node].begin(),
            adjacency[node].end(),
            node
        ) != adjacency[node].end();
    }
    return {std::move(component_id), std::move(members), std::move(cyclic)};
}

class CycleSearch {
public:
    CycleSearch(
        int modulus,
        const std::vector<std::vector<int>>& adjacency,
        const std::vector<std::vector<int>>& supports,
        const Components& components,
        CubeOracle& cube,
        Stats& layer,
        Stats& total,
        CycleWitness& first_direct,
        CycleWitness& first_multiplier
    )
        : modulus_(modulus),
          adjacency_(adjacency),
          supports_(supports),
          components_(components),
          cube_(cube),
          layer_(layer),
          total_(total),
          first_direct_(first_direct),
          first_multiplier_(first_multiplier),
          visited_(adjacency.size(), false) {}

    void run_component(int component_id) {
        const std::vector<int>& members = components_.members[component_id];
        for (const int start : members) {
            std::fill(visited_.begin(), visited_.end(), false);
            visited_[start] = true;
            path_ = {start};
            search(start, start, supports_[start], component_id);
        }
    }

private:
    void search(
        int start,
        int node,
        const std::vector<int>& current_support,
        int component_id
    ) {
        if (cube_.hits_minus_one(current_support)) {
            return;
        }
        for (const int destination : adjacency_[node]) {
            if (
                components_.id[destination] != component_id
                || destination < start
            ) {
                continue;
            }
            if (destination == start) {
                ++layer_.direct_radical_miss_cycles;
                ++total_.direct_radical_miss_cycles;
                if (first_direct_.empty()) {
                    first_direct_ = {modulus_, path_, current_support};
                }
                if (!cube_.hits_multiplier_targets(current_support)) {
                    ++layer_.multiplier_bridge_miss_cycles;
                    ++total_.multiplier_bridge_miss_cycles;
                    if (first_multiplier_.empty()) {
                        first_multiplier_ = {modulus_, path_, current_support};
                    }
                }
                continue;
            }
            if (visited_[destination]) {
                continue;
            }
            visited_[destination] = true;
            path_.push_back(destination);
            search(
                start,
                destination,
                merge_support(current_support, supports_[destination]),
                component_id
            );
            path_.pop_back();
            visited_[destination] = false;
        }
    }

    int modulus_;
    const std::vector<std::vector<int>>& adjacency_;
    const std::vector<std::vector<int>>& supports_;
    const Components& components_;
    CubeOracle& cube_;
    Stats& layer_;
    Stats& total_;
    CycleWitness& first_direct_;
    CycleWitness& first_multiplier_;
    std::vector<char> visited_;
    std::vector<int> path_;
};

void write_vector(std::ostream& output, const std::vector<int>& values) {
    output << '[';
    for (std::size_t index = 0; index < values.size(); ++index) {
        if (index != 0) {
            output << ',';
        }
        output << values[index];
    }
    output << ']';
}

void write_stats(std::ostream& output, const Stats& stats) {
    output
        << "\"moduli\":" << stats.moduli << ','
        << "\"cyclic_moduli\":" << stats.cyclic_moduli << ','
        << "\"cyclic_components\":" << stats.cyclic_components << ','
        << "\"cyclic_nodes\":" << stats.cyclic_nodes << ','
        << "\"dangerous_components\":" << stats.dangerous_components << ','
        << "\"direct_radical_miss_cycles\":"
        << stats.direct_radical_miss_cycles << ','
        << "\"multiplier_bridge_miss_cycles\":"
        << stats.multiplier_bridge_miss_cycles;
}

void write_witness(std::ostream& output, const CycleWitness& witness) {
    if (witness.empty()) {
        output << "null";
        return;
    }
    output << "{\"R\":" << witness.modulus << ",\"cycle\":";
    write_vector(output, witness.cycle);
    output << ",\"support\":";
    write_vector(output, witness.support);
    output << '}';
}

}  // namespace

int main(int argc, char** argv) {
    const int limit = argc >= 2 ? std::stoi(argv[1]) : 100000;
    const std::string output_path = argc >= 3 ? argv[2] : "";
    if (limit < 7) {
        std::cerr << "limit must be at least 7\n";
        return 2;
    }
    const auto started = std::chrono::steady_clock::now();

    std::vector<int> spf(static_cast<std::size_t>(limit) + 1);
    std::iota(spf.begin(), spf.end(), 0);
    std::vector<int> primes;
    for (int prime = 2; prime <= limit; ++prime) {
        if (spf[prime] != prime) {
            continue;
        }
        primes.push_back(prime);
        if (static_cast<long long>(prime) * prime > limit) {
            continue;
        }
        for (
            long long value = static_cast<long long>(prime) * prime;
            value <= limit;
            value += prime
        ) {
            if (spf[static_cast<std::size_t>(value)] == value) {
                spf[static_cast<std::size_t>(value)] = prime;
            }
        }
    }

    Stats total;
    std::map<int, Stats> layers;
    CycleWitness first_direct;
    CycleWitness first_multiplier;

    for (int modulus = 7; modulus <= limit; modulus += 8) {
        Stats& layer = layers[((modulus - 1) / 10000 + 1) * 10000];
        ++layer.moduli;
        ++total.moduli;
        const int maximum_node = (modulus - 1) / 2;
        std::vector<std::vector<int>> adjacency(
            static_cast<std::size_t>(maximum_node) + 1
        );
        std::vector<char> active(adjacency.size(), false);

        for (const int prime : primes) {
            const long long square = static_cast<long long>(prime) * prime;
            if (square >= modulus) {
                break;
            }
            if (modulus % prime == 0) {
                continue;
            }
            for (
                int coordinate = static_cast<int>(square);
                coordinate < modulus;
                coordinate += static_cast<int>(square)
            ) {
                if (std::gcd(coordinate, modulus) != 1) {
                    continue;
                }
                const int source = std::min(coordinate, modulus - coordinate);
                const int reduced = coordinate / prime;
                const int destination = std::min(reduced, modulus - reduced);
                adjacency[source].push_back(destination);
                active[source] = true;
                active[destination] = true;
            }
        }
        for (auto& destinations : adjacency) {
            std::sort(destinations.begin(), destinations.end());
            destinations.erase(
                std::unique(destinations.begin(), destinations.end()),
                destinations.end()
            );
        }

        const Components all = strongly_connected_components(adjacency, active);
        std::vector<int> cyclic_components;
        std::vector<char> cyclic_node(adjacency.size(), false);
        for (std::size_t id = 0; id < all.members.size(); ++id) {
            if (!all.cyclic[id]) {
                continue;
            }
            cyclic_components.push_back(static_cast<int>(id));
            for (const int node : all.members[id]) {
                cyclic_node[node] = true;
            }
        }
        if (cyclic_components.empty()) {
            continue;
        }
        ++layer.cyclic_moduli;
        ++total.cyclic_moduli;
        layer.cyclic_components += static_cast<std::int64_t>(
            cyclic_components.size()
        );
        total.cyclic_components += static_cast<std::int64_t>(
            cyclic_components.size()
        );

        CubeOracle cube(modulus);
        std::vector<std::vector<int>> supports(adjacency.size());
        std::vector<char> dangerous(adjacency.size(), false);
        for (const int component_id : cyclic_components) {
            for (const int node : all.members[component_id]) {
                ++layer.cyclic_nodes;
                ++total.cyclic_nodes;
                supports[node] = node_support(node, modulus, spf);
                dangerous[node] = !cube.hits_minus_one(supports[node]);
            }
        }

        const Components reduced = strongly_connected_components(
            adjacency,
            dangerous
        );
        CycleSearch search(
            modulus,
            adjacency,
            supports,
            reduced,
            cube,
            layer,
            total,
            first_direct,
            first_multiplier
        );
        for (std::size_t id = 0; id < reduced.members.size(); ++id) {
            if (!reduced.cyclic[id]) {
                continue;
            }
            ++layer.dangerous_components;
            ++total.dangerous_components;
            search.run_component(static_cast<int>(id));
        }
    }

    if (limit == 100000) {
        if (
            total.moduli != 12500
            || total.cyclic_moduli != 511
            || total.cyclic_components != 807
            || total.cyclic_nodes != 9809
            || total.direct_radical_miss_cycles != 1
            || total.multiplier_bridge_miss_cycles != 0
            || first_direct.modulus != 30031
            || first_direct.cycle != std::vector<int>({31, 6000, 1200, 240, 961})
        ) {
            std::cerr << "locked 100000-prefix result changed\n";
            return 3;
        }
    }

    std::ofstream output_file;
    std::ostream* output = &std::cout;
    if (!output_path.empty()) {
        output_file.open(output_path);
        if (!output_file) {
            std::cerr << "could not open output path\n";
            return 2;
        }
        output = &output_file;
    }
    *output
        << "{\n"
        << "  \"arithmetic\": \"Complete SCC scan of every R=7 mod 8 up to the limit; "
           "enumerate only simple cycles whose accumulated coordinate support still "
           "misses -1, then test -1, -4B, and -(4B)^-1 in the signed radical cube.\",\n"
        << "  \"limit\":" << limit << ",\n"
        << "  \"residue_class\":\"R=7 mod 8\",\n"
        << "  \"summary\":{";
    write_stats(*output, total);
    *output << "},\n  \"layers\":[\n";
    bool first_layer = true;
    for (const auto& [upper, stats] : layers) {
        if (!first_layer) {
            *output << ",\n";
        }
        first_layer = false;
        *output << "    {\"upper\":" << std::min(upper, limit) << ',';
        write_stats(*output, stats);
        *output << '}';
    }
    *output << "\n  ],\n  \"first_direct_radical_miss\":";
    write_witness(*output, first_direct);
    *output << ",\n  \"first_multiplier_bridge_miss\":";
    write_witness(*output, first_multiplier);
    *output << "\n}\n";

    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started
    ).count();
    std::cerr << "elapsed_seconds=" << elapsed << '\n';
    return 0;
}
