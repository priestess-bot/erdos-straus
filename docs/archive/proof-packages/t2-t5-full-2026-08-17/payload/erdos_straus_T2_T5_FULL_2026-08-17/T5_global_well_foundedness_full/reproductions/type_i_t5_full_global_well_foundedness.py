#!/usr/bin/env python3
"""Focused verifier for T5 full contract-level well-foundedness.

This verifies the common rank algebra and the historical cycle exclusions.  It does not replace
source-specific E1--E4 arithmetic verifiers.  T5 admission is evaluated only after E1--E4.
"""
from dataclasses import dataclass
from enum import IntEnum

class Major(IntEnum):
    GENERIC_MARKED = 1
    TYPEI = 2
    TYPEII_G_HANDOFF = 3
    TYPEII_REL = 4

class Protocol(IntEnum):
    NONE = 0
    RESET = 1
    ABSORB = 2
    PRE = 3
    CHARGED = 4

@dataclass(frozen=True)
class State:
    rho: int
    major: Major
    protocol: Protocol = Protocol.NONE
    p: int = 73
    q: int = 0
    A: int = 1
    K: int = 1
    eta: int = 0
    a: int = 0
    R: int = 0
    m: int = 0
    r_eps: int = 0
    reset_M: int = 0

    def __post_init__(self):
        if self.rho < 0:
            raise ValueError("rho must be nonnegative")
        if self.major != Major.TYPEI and self.protocol != Protocol.NONE:
            raise ValueError("non-Type-I states cannot carry Type-I protocol")
        if self.major == Major.TYPEII_REL and self.q < 1:
            raise ValueError("TYPEII_REL requires q>=1")
        if self.major == Major.TYPEI:
            if self.protocol == Protocol.NONE:
                raise ValueError("TYPEI requires a protocol")
            if self.protocol == Protocol.CHARGED and (self.A < 1 or self.K < 1 or self.K % self.A):
                raise ValueError("CHARGED requires A|K")
            if self.protocol == Protocol.RESET and self.reset_M < 1:
                raise ValueError("RESET requires positive carrier M")

    @property
    def Bp(self):
        return ((self.p - 1) ** 2) // 4

    def local(self):
        if self.major == Major.TYPEII_REL:
            return (self.q, 0, 0, 0)
        if self.major == Major.TYPEII_G_HANDOFF:
            return (0, 0, 0, 0)
        if self.major == Major.GENERIC_MARKED:
            return (0, 0, 0, 0)
        if self.protocol == Protocol.CHARGED:
            return (self.Bp // self.A, self.K // self.A, self.eta, 0)
        if self.protocol == Protocol.PRE:
            return (self.a, 0, 0, 0)
        if self.protocol == Protocol.ABSORB:
            return (self.R, self.m, self.r_eps, 0)
        if self.protocol == Protocol.RESET:
            return (self.reset_M, 0, 0, 0)
        raise AssertionError("unreachable")

    def rank(self):
        return (self.rho, int(self.major), int(self.protocol), *self.local())


def strict(s, t):
    return t.rank() < s.rank()


def charged(p=73, A=1, C=1, eta=0, rho=None):
    return State(rho=p if rho is None else rho, major=Major.TYPEI, protocol=Protocol.CHARGED,
                 p=p, A=A, K=A*C, eta=eta)


def verify():
    # TYPE-II F->F q descent.
    s = State(1009, Major.TYPEII_REL, p=1009, q=18)
    t = State(1009, Major.TYPEII_REL, p=1009, q=6)
    assert strict(s,t)
    assert not strict(t,s)

    # TYPE-II endpoint reclassified as G: phase drop pays even before a handoff exists.
    g = State(1009, Major.TYPEII_G_HANDOFF, p=1009)
    assert strict(s,g)

    # G -> Type-I root: phase drop.  Positive-q G would use exactly the same T5 rule if E1--E4 is found.
    root = charged(1009,A=1,C=5000)
    assert strict(g,root)
    assert not strict(root,g)

    # CHARGED support growth: J drops; later fields may reset.
    p=73
    low = charged(p,A=2,C=10)
    bigger_support = charged(p,A=6,C=999)
    assert strict(low,bigger_support)

    # Same-chart high-support promotion: J can stay 0, C must drop.
    B=((p-1)**2)//4
    hs = charged(p,A=B+10,C=45)
    hs2 = charged(p,A=2*(B+10),C=44)
    assert strict(hs,hs2)
    assert not strict(hs,charged(p,A=2*(B+10),C=47))

    # d=1 regeneration: J,C fixed, eta strictly drops.
    reg1 = charged(p,A=B+10,C=p-1,eta=1)
    reg0 = charged(p,A=B+10,C=p-1,eta=0)
    assert strict(reg1,reg0)
    assert not strict(reg0,reg1)

    # T2 H4 / high-C=2 macro pattern: p-1 -> <=p-2 at high support.
    h4 = charged(p,A=2*(B+10),C=67)
    assert strict(charged(p,A=B+10,C=p-1),h4)

    # PRE rank and one-way PRE->ABSORB.
    pre2 = State(p,Major.TYPEI,Protocol.PRE,p=p,a=2)
    pre1 = State(p,Major.TYPEI,Protocol.PRE,p=p,a=1)
    absorb = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=71,m=10,r_eps=5)
    assert strict(pre2,pre1)
    assert strict(pre1,absorb)  # protocol 3 -> 2
    assert not strict(absorb,pre1)

    # ABSORB local schedule.
    abR = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=71,m=10,r_eps=5)
    abR2 = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=35,m=999,r_eps=999)
    assert strict(abR,abR2)  # R first
    abm = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=35,m=9,r_eps=999)
    assert strict(abR2,abm)  # m after same R
    abr = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=35,m=9,r_eps=4)
    assert strict(abm,abr)

    # Historical PRE/inverse two-cycle cannot be recursive in both directions.
    # X->Y may be PRE; Y->X would require ABSORB->PRE and is rejected by rank.
    X = State(p,Major.TYPEI,Protocol.PRE,p=p,a=2)
    Y = State(p,Major.TYPEI,Protocol.PRE,p=p,a=1)
    Y_abs = State(p,Major.TYPEI,Protocol.ABSORB,p=p,R=71,m=1,r_eps=1)
    assert strict(X,Y)
    assert strict(Y,Y_abs)
    assert not strict(Y_abs,X)

    # RESET is absorbing at fixed rho: enter it downward, stay only with M drop, no return.
    charged38 = charged(p,A=1,C=38)
    reset12 = State(p,Major.TYPEI,Protocol.RESET,p=p,reset_M=12)
    reset10 = State(p,Major.TYPEI,Protocol.RESET,p=p,reset_M=10)
    assert strict(charged38,reset12)
    assert strict(reset12,reset10)
    # The historical re-entry 12 -> 132 would require RESET->CHARGED (or M increase inside RESET).
    reentered132 = charged(p,A=1,C=132)
    reset132 = State(p,Major.TYPEI,Protocol.RESET,p=p,reset_M=132)
    assert not strict(reset12,reentered132)
    assert not strict(reset12,reset132)

    # A paid joined-support reset should remain CHARGED and lower J, not use RESET.
    joined_src=charged(p,A=19,C=22)
    joined_dst=charged(p,A=38,C=999)
    assert strict(joined_src,joined_dst)

    # Standalone stutter is not an edge.
    same = charged(p,A=B+10,C=45)
    assert not strict(same,same)

    # Smaller induction rank can reset all phases/protocol/local fields.
    outer_src=State(1009,Major.TYPEI,Protocol.RESET,p=1009,reset_M=1)
    outer_dst=State(997,Major.TYPEII_REL,p=1009,q=10**9)
    assert strict(outer_src,outer_dst)

    # GENERIC_MARKED cannot recurse at same rho under v2; only outer rank drop can move it.
    gm=State(100,Major.GENERIC_MARKED,p=1009)
    gm_same=State(100,Major.GENERIC_MARKED,p=1009)
    gm_small=State(99,Major.GENERIC_MARKED,p=1009)
    assert not strict(gm,gm_same)
    assert strict(gm,gm_small)

    print("T5 FULL contract-level global well-foundedness controls passed")

if __name__ == "__main__":
    verify()
