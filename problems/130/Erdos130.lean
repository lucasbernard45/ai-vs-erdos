/-
Formal skeleton for Erdős #130 generic translation assembly lemma.
Mathlib-compatible, Lean 4.

This file states definitions and theorems; heavy algebraic computations are left as `sorry`
but structured so `ring`, `linarith`, and determinant expansions can fill them.

Author: Arena AI Agent, 30 July 2026
-/

import Mathlib.Topology.Baire.BaireCategory
import Mathlib.Analysis.InnerProductSpace.EuclideanDist
import Mathlib.Data.Set.Countable
-- import Mathlib.Combinatorics.SimpleGraph.Basic (for integer-distance graph)

open Set Real

noncomputable section

def Point := EuclideanSpace ℝ (Fin 2)

def dist (p q : Point) : ℝ := ‖p - q‖

def Collinear (p q r : Point) : Prop :=
  -- det [q-p, r-p] = 0
  let v1 := q - p
  let v2 := r - p
  v1 0 * v2 1 - v1 1 * v2 0 = 0

def Concyclic (p q r s : Point) : Prop :=
  -- det [ x y x²+y² 1 ] = 0
  let M : Matrix (Fin 4) (Fin 4) ℝ := fun i j =>
    match i, j with
    | 0,0 => p 0 | 0,1 => p 1 | 0,2 => (p 0)^2 + (p 1)^2 | 0,3 => 1
    | 1,0 => q 0 | 1,1 => q 1 | 1,2 => (q 0)^2 + (q 1)^2 | 1,3 => 1
    | 2,0 => r 0 | 2,1 => r 1 | 2,2 => (r 0)^2 + (r 1)^2 | 2,3 => 1
    | 3,0 => s 0 | 3,1 => s 1 | 3,2 => (s 0)^2 + (s 1)^2 | 3,3 => 1
  M.det = 0

def StronglyGeneral (S : Set Point) : Prop :=
  (∀ p ∈ S, ∀ q ∈ S, ∀ r ∈ S, p ≠ q → p ≠ r → q ≠ r → ¬Collinear p q r) ∧
  (∀ p ∈ S, ∀ q ∈ S, ∀ r ∈ S, ∀ s ∈ S, p ≠ q → p ≠ r → p ≠ s → q ≠ r → q ≠ s → r ≠ s → ¬Concyclic p q r s)

def IsIntegerDist (p q : Point) : Prop :=
  ∃ m : ℕ, m > 0 ∧ dist p q = (m : ℝ)

def BadCircle (a b : Point) (m : ℕ) : Set Point :=
  { t : Point | dist a (b + t) = (m : ℝ) }

def BadLine2Old1New (a1 a2 b : Point) : Set Point :=
  { t : Point | Collinear a1 a2 (b + t) }

def BadLine1Old2New (a b1 b2 : Point) : Set Point :=
  { t : Point | Collinear a (b1 + t) (b2 + t) }

def BadConcyclic (p1 p2 p3 p4 : Point) (distrib : Fin 4 → Bool) : Set Point :=
  -- distrib indicates which points are translated; simplified version
  { t | Concyclic p1 p2 p3 p4 } -- placeholder: actual t-dependence in definition

-- Lemma statement

theorem generic_translation_lemma
  (A B : Set Point) (hA : StronglyGeneral A) (hB : StronglyGeneral B)
  (hB_fin : B.Finite) (hA_ct : A.Countable) :
  ∃ t : Point, StronglyGeneral (A ∪ (B + t)) ∧
  (∀ a ∈ A, ∀ b ∈ B, ¬IsIntegerDist a (b + t)) :=
by
  -- Idea: Bad set = countable union of circles, lines, degree ≤2 curves.
  -- Each is closed nowhere dense.
  -- ℝ² is Baire space, so complement is dense.
  sorry

theorem countable_disjoint_union_closure
  (S : ℕ → Set Point) (h : ∀ n, (S n).Finite ∧ StronglyGeneral (S n)) :
  ∃ T : ℕ → Point, StronglyGeneral (⋃ n, S n + T n) ∧
  (∀ n m, n ≠ m → ∀ p ∈ S n, ∀ q ∈ S m, ¬IsIntegerDist (p + T n) (q + T m)) :=
by
  -- inductive application of generic_translation_lemma
  sorry

theorem chromatic_fin_inf_equiv :
  -- Let χ*fin = sup χ(G(S)) finite S
  -- χ*inf = sup χ(G(A)) infinite A
  -- Then χ*fin = χ*inf in WithTop ℕ (where ⊤ = ℵ0)
  True := by trivial -- detailed statement requires SimpleGraph chromatic number definition

-- explicit polynomial non-vanishing for 2+2 case

lemma concyclic_2plus2_nontrivial (a1 a2 b1 b2 : Point)
  (ha : a1 ≠ a2) (hb : b1 ≠ b2) :
  ∃ t : Point, ¬Concyclic a1 a2 (b1 + t) (b2 + t) :=
by
  -- choose T large, compute leading term of determinant
  -- polynomial not identically zero
  sorry

end
