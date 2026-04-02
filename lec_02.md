# State and Observables

## 1. Differences between Particle Trajetory World in Classical Mechanics and Wave Function Fields in Quantum Mechanics

| Classical mechanics | Quantum mechanics |
| --- | --- |
| Particles do have explicit trajectory $x(t)$ | Without trajectory |
| State = $(x, p)$ | State = wave-function $\Psi(x)$ |
| Position & momentum simultaneously measured | $[\hat{x}, \hat{p}] = i \hbar$ non-commuting |
| Determinism | Probability theory (Born rule) |
| Particle is point | Particle in a field |

### Classical

**1. In classical mechanics**
- World consist of particles,
- particles move in space,
- they have explicit trajectories.

It also refer to enabling predicting the future when the initial conditions (location and velocity) are known. In consequence, classical mechanics is deterministic.

The motion of classical particles is determined by the equations of motion.

$$F = ma$$ or $$F = \frac{dP}{dt}$$ or $$F = - \frac{du}{dx}$$

where,
- $m$, Mass of particles or substances, unit $kg$,
- $a$, acceleration of particles or substances, $a = \frac{dv}{dt}$, unit $m/s^2$,
- $P$, momentum, $p = mv$, unit $kg \cdot m/s$
- $t$, motion time, unit $s$,
- $\frac{dP}{dt}$, the rate of change of momentum with respect to time, it is more accurate because of change of substances during moving.
- $u$, potential energy, gravitational potential energy $U = mgh$, spring potential energy $U = \frac{1}{2} kx^2$, unit Joule, $J$,
- $- \frac{du}{dx}$, spatial gradient of potential energy, force is equal to the rate of decrease of potential energy in the spatial direction, the minus means that the direction of the force always points towards the direction of decreasing potential energy.

**2. Nonlinear problems may not be unique**

A complex nonlinear system possibly exist multiple solutions, and it is extremely sensitive to initial conditions.

For example, there are 2 tiny different initial conditions of bullet trajectories because of gun shaking, $x_1$ and $x_2$, the difference is explained,

$$\Delta x(0) = x_2(0) - x_1(0)$$

where,
- 0 means that the motion time is zero, $t = 0$.

In future, there is a huge difference between the final trajectory at the time $t$,

$$\Delta x(0) \rightarrow huge \ \Delta x(t)$$

Even so, classical physics still maintains that particles "do have trajectories", which cannot be just accurately computed.

**3. Phase space: position + momemtum**

Phase space means that a (group of) particle exist(s) in a 3-dimensional space, and it has a location $(x, y, z)$ and a momentum $(p_x, p_y, p_z)$. Now, here are 6 variables $(x, y, z, p_x, p_y, p_z)$, therefore,

$$phase space = \mathbb{R}^6$$

**4. Liouville theorem: phase space volume conserved**

If there is a group of particles, which concentrate on a small region of phase space under initial condition. As the time changes, this region might be stretched and distorted, but its volume will remain unchanged.

$$\frac{d V_p}{dt} = 0$$

### Quantum

**1. No well-defined trajectories in quantum mechanics**

In quantum mechanics, we no longer have well defined trajectories $x(t)$. The reason why no longer defined trajectory exists is that nature does not allow a trajectory.

**2. Position and momentum are non-commuting**

***2.1. What is commuting or non-commuting?***

2 operations can be performed in either order, and the result is the same.

**Commuting in basic algebra**:

The multiplication of real numbers is commuting,

$$ab = ba$$

**Commuting operators**:

In quantum mechanics or linear algebra, we deal with operators $A, B$,

$$AB = BA$$

Equivalent definition using the commutator:

$$[A, B] = AB - BA$$

where,
- if $[A, B] = 0$, then $A$ and $B$ commute.
- if $[A, B] \ne 0$, they do not commute.

For examples, commuting matrices，let,

$$A= \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix},
\quad
B= \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}$$

Then,

$$AB = BA$$

So these matrices commute, or it can be descirbed that is *simultaneous diagonalization*. However, if,

$$A= \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix},
\quad
B= \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$$

Then,

$$AB \ne BA$$

So they do not commute.

*Physical meaninig in quantum mechanics, if 2 observables commute:*

$$[A, B] = 0$$

then,
- they can be measured simultaneously,
- they share common eigenstates,
- there is no uncertainty tradeoff.

*An example, commuting quantum gates,*

$$U_1 U_2 = U_2 U_1$$

and a deeper example, gates acting on different qubits commute:

$$(X \otimes I)(I \otimes Z) = (I \otimes Z)(X \otimes I)$$

***2.2 Position and momentum do NOT commut***

In quantum mechanics,
- position is not a number, but an operator $\hat{x}$,
- momentum is not a number, but an operator $\hat{p}$.

They meet,

$$[\hat{x}, \hat{p}] \ne 0$$

more specific,

$$[\hat{x}, \hat{p}] = i \hbar$$

It is called non-commuting, it means,
- they cannot be simultaneously measured exactly, 
- the position of particles is unknown,
- the momentum of particles is unknown.

In consequence, you don't know the trajectory because the trajectory ask you to simultaneously know $x$ and $p$.

Or,

$$\Delta x \Delta p \ge \frac{\hbar}{2}$$

The final summary is that the trajectory does not exist, this is the origin of **Heisenberg's uncertainty principle**.

**3. Wavefunction description: quantum state is "wave"**

***3.1. Quantum mechanics describe wave, instead trajectory.***

Wave function decribe the probability amplitude, instead of the position of particles.

$$|\Psi(x)|^2 = P(x)$$

it means that the probability density that the particles exist at the position x.

***3.2. Waves are field-like quantities.***

Waves are fields,
- electromagnetic waves: elecric field $E(x,y)$,
- water waves: height $h(x,t)$.

They have features,
- they are not a point in space,
- they distribute in the area.

So,

$$\Psi(x)$$

is also the defined function in the whole space,
- it is not a particle existing at the specific point position,
- but rather a wave description of the particle "potentially being everywhere".

*Quantum states are "extended," not "point-like".*

***3.3. Wavefunction Ψ(x) itself as a field***

Hence, the research fundamental objects of quantum mechanics is itself as a field, instead of a trajectory. It tells that,
- how are particles distributed?
- how do measurement probabilities arise?
- how do interference and diffraction occur?
- how is entanglement possible?

***3.4. Born rule***

In quantum mechanics, wave-function itself is not the result. A rule transfer it from a function to probability.

The meaning of this rule is that, the result of measurement is not deterministic, but rather a random variable whose distribution is given by the Born rule. In other word, *Bron rule is the probability distribution definition of quantum mechanics*.

So now, the rule transfer the quantum state into the probability space. In probability theory, a random experiment requires 3 stuffs,

$$(\Omega, \mathcal{F}, P)$$

where,
- $\Omega$, all possible results in sample space,
- $\mathcal{F}$, an event set,
- $P$, the probability measure.

Quantum state,

$$|\psi\rangle= \sum_i a_i |i\rangle$$

Bron rule,

$$P(i) = |a_i|^2$$ with quantum state normalization, $$\sum_i |a_i|^2 = 1$$

## 2. Hilbert Space

It is the vector space containing quantum state.

The system state is not a point, but rather a wave-functon,

$$\psi(x)$$ or a vector, $$|\psi\rangle$$ in Hilbert Space that is defined a space can contain these vector calculation, $$\mathcal{H}$$, which means,
- state can be superimposed,
- state can rotated,
- state can projected,
- state can be interfere.

**Hilbert space critical mathematical definition**

*1. Vector space*

If $$|\psi\rangle, |\phi\rangle \in \mathcal{H}$$ and to any random complex numbers $a$, $b$, $$a|\psi\rangle + b|\phi\rangle \in \mathcal{H}$$

The above is superposition, because

$$|\psi\rangle = c|0\rangle + d |1\rangle$$ and $$|\phi\rangle = e|0\rangle + f|1\rangle$$

*2. Inner product*

Inner product in Hilbert Space, bra and ket, $$\langle\psi|\phi\rangle$$

and it will give the norm, $$\||\psi\rangle\|^2 = \langle\psi|\phi\rangle$$

orthogonality, $$\langle 0|1 \rangle = 0$$

born rule, $$P(i) = |\langle i|\psi \rangle|^2$$

*3. Completeness*

Hilbert space is not a physical space.

Hilbert space is infinite dimension. The relationship between the number of qubit and dimension, $$dim(\mathcal{H}) = 2^n$$

*4. Hilbert space basis expansion*

Geometric interpretation: the components of a vector along the coordinate axes.

Space basis is vector basis, in classical,

$$\vec{v} = x \hat{e_1} + y \hat{e_2}$$

with $\hat{e_1} = (1, 0)$ and $\hat{e_2} = (0, 1)$, these 2 are normal vector space basis.

In quantum, a set of basis,

$$\{|e_1\rangle, |e_2\rangle, |e_3\rangle, \cdots \}$$

If ${|e_i\rangle}$ was an orthonormal basis of a Hilbert space, $$\langle e_i|e_j \rangle = \delta_{ij}$$ so random quantum state, $$|\psi\rangle = \sum_i{c_i |e_i\rangle}$$ and $$c_i = \langle e_i|\psi \rangle$$ or $c_i$ could be described that the projection length of state onto the basis direction (probability amplitude).

Here's 3 different types of basis: position basis, energy basis, and spin basis.

## 3. Qubit

### Definition

A qubit is a two-level quantum system whose pure states are represented in a two-dimensional complex Hilbert space in quantum mechanics.

In mathematics, it is a complex vector space, $$\mathcal{H} = \mathbb{C}^2$$

It has 2 basises $|0\rangle$ and $|1\rangle$.

They are like cbit, $0$ or $1$.

However, qubit can be superimposed. The expression is same as the above,

$$|\psi\rangle = a|0\rangle + b|1\rangle$$ with $$a,b \in \mathbb{C}$$ and must be normalized, $$|a|^2 + |b|^2 = 1$$

where,
- $a$, $b$, complex-valued probability amplitudes, they are not the real probability, but they determine probabilities after measurement,
- $|\psi\rangle$ is state vector of qubit.

### Meaning of Physics

Measurement, $$P(0) = |a|^2, P(1) = |b|^2$$.

### In Bloch Sphere

Any random single qubit's pure state, the derivation process,

$$|\psi\rangle = |a|e^{iy}|0\rangle + |b|e^{i\delta}|1\rangle$$

$$\Rightarrow |\psi\rangle = e^{iy} (|a||0\rangle + |b|e^{i\phi}|1\rangle)$$

$e^{iy}$ is a global phase for rotation, which is irrelevant,

$$\Rightarrow |\psi\rangle = |a||0\rangle + |b|e^{i\phi}|1\rangle$$

$$\Rightarrow |\psi\rangle = cos\frac{\theta}{2}|0\rangle + e^{i\phi}sin\frac{\theta}{2}|1\rangle$$

where,
- $\theta$ is polar angle, which manage z direction in bloch sphere,
- $\phi$ is azimuthal phase angle, which manage xy direction in bloch sphere,
- $e^{i\phi}$ is the complex phase.

$\phi$ and $e^{i\phi}$ would not affect the probability, they only change the direction of amplitudes.