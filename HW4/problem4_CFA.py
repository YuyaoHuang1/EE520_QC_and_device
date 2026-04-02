x = 2.94857295039273
TARGET_PRECISION = 1e-5

# Step 1: CFA iterations
print("=" * 60)
print("Step 1: Continued Fraction Algorithm (CFA) iterations")
print("=" * 60)
print(f"{'n':>4}  {'x_n':>22}  {'a_n':>4}  {'remainder':>22}")
print("-" * 60)

phi = x
coeffs = []
for n in range(10):
    a_n = int(phi)
    remainder = phi - a_n
    print(f"{n:>4}  {phi:>22.15f}  {a_n:>4}  {remainder:>22.15f}")
    coeffs.append(a_n)
    if remainder < 1e-10:
        break
    phi = 1.0 / remainder

print()
print(f"Continued fraction: x = [{coeffs[0]}; {', '.join(map(str, coeffs[1:]))}]")

# Step 2: Compute convergents
print()
print("=" * 60)
print("Step 2: Convergents  p_n/q_n")
print("  Recurrence: p_n = a_n * p_{n-1} + p_{n-2}")
print("              q_n = a_n * q_{n-1} + q_{n-2}")
print("  Init: p_{-1}=1, p_0=a_0,  q_{-1}=0, q_0=1")
print("=" * 60)
print(f"{'n':>3}  {'a_n':>4}  {'p_n':>6}  {'q_n':>6}  {'p_n/q_n':>20}  {'error':>12}")
print("-" * 60)

p_prev, p_curr = 1, coeffs[0]
q_prev, q_curr = 0, 1
err = abs(p_curr / q_curr - x)
print(f"{0:>3}  {coeffs[0]:>4}  {p_curr:>6}  {q_curr:>6}  {p_curr/q_curr:>20.15f}  {err:>12.3e}")

answer_n, answer_p, answer_q = None, None, None

for n in range(1, len(coeffs)):
    a = coeffs[n]
    p_next = a * p_curr + p_prev
    q_next = a * q_curr + q_prev
    err = abs(p_next / q_next - x)
    print(f"{n:>3}  {a:>4}  {p_next:>6}  {q_next:>6}  {p_next/q_next:>20.15f}  {err:>12.3e}")
    p_prev, p_curr = p_curr, p_next
    q_prev, q_curr = q_curr, q_next
    if answer_n is None and err < TARGET_PRECISION:
        answer_n, answer_p, answer_q = n, p_next, q_next

# Step 3: Theorem A4.15 verification
print()
print("=" * 60)
print("Step 3: Theorem A4.15 verification")
print("  Condition: |p/q - x| <= 1/(2*q^2)  implies p/q is a convergent")
print("=" * 60)

p, q = answer_p, answer_q
approx_error = abs(p / q - x)
theorem_bound = 1 / (2 * q**2)

print(f"  Best convergent meeting 5-decimal accuracy: n = {answer_n}")
print(f"  p = {p},  q = {q}")
print(f"  p/q = {p}/{q} = {p/q:.15f}")
print(f"  |p/q - x|     = {approx_error:.6e}")
print(f"  1 / (2*q^2)   = 1 / (2 * {q}^2) = 1/{2*q*q} = {theorem_bound:.6e}")
print(f"  Condition satisfied: {approx_error:.6e} < {theorem_bound:.6e}  -->  {approx_error < theorem_bound}")

print()
print("=" * 60)
print("Final Answer")
print("=" * 60)
print(f"  p/q = {p}/{q}  ~  {p/q:.10f}")
print(f"  Error ~ {approx_error:.3e}  <  10^-5")
print(f"  The rational approximation {p}/{q} is correct to 5 decimal places.")
