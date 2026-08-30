## **ML Example Workouts and Statistical Concepts**

<img width="1027" height="596" alt="image" src="https://github.com/user-attachments/assets/cad271d6-6e35-42bd-8873-16cd6dc03e79" />


<img width="1387" height="522" alt="image" src="https://github.com/user-attachments/assets/7e305364-6c4e-4ed6-b51c-32398f066c28" />


<img width="1217" height="843" alt="image" src="https://github.com/user-attachments/assets/d4515888-21fa-4cb3-82fa-b3a947fe2805" />

The example workout that we performed is for single layer perceptron. 

If we added even one hidden layer:
            The model becomes a multi-layer perceptron (MLP), Can solve XOR, Requires backpropagation, Loses the Perceptron Convergence Theorem guarantee


**4. Evaluation Metrics:-**

<img width="1838" height="855" alt="image" src="https://github.com/user-attachments/assets/f9b9fd28-2cc7-44e0-9cc3-09c89fe4ba0b" />

<p></p>
<p></p>
 
**5. Eigen Value Spectrum**

<img width="1852" height="762" alt="image" src="https://github.com/user-attachments/assets/04335a57-efe6-4920-bc4b-39c52faacd8c" />



## Statistics
- Probability distributions  
- Conditional probability  
- Expectation (Expected value)  
- Entropy  
- Cross-entropy loss  
- KL-divergence  
- Sampling & negative sampling

Statistical Concepts in LSTM, xLSTM, Transformer, TiREX, and Mamba Models:-

<img width="1357" height="582" alt="image" src="https://github.com/user-attachments/assets/2fd58c59-248a-4bba-a8dd-a2b648f40cb4" />

<img width="467" height="457" alt="image" src="https://github.com/user-attachments/assets/367fb731-3d5d-454d-9232-ff80b4b89c2f" />

**Entropy:-** Entropy measures the uncertainty or randomness of a single probability distribution. Entropy looks only at the true (or predicted) distribution itself, not at a comparison. {How unsure is this distribution?”}

A uniform distribution → high entropy (very uncertain), A peaked distribution → low entropy (confident)

**Cross-entropy** Cross-entropy measures how far one probability distribution is from another — typically, how well a model’s predictions match the true labels.


## Linear Algebra
- Basis and change of basis  
- Vector spaces and subspaces  
- Orthogonality  
- Matrix rank  
- Inverse & pseudo-inverse  
- Diagonalization  
- Singular Value Decomposition (SVD)  

## Optimization & Calculus (Light Awareness)
- Gradients  
- Partial derivatives  
- Chain rule  
- Gradient descent  

## Sequence & Modeling
- Time steps & sequence length  
- Masking  
- Positional encoding  

## Numerical & Practical
- Normalization & standardization  
- Numerical stability  
- Floating-point precision  

--------------------------

--------------------------


## Orders of statistics 

Orders of statistics are unlimited in theory, but typically only up to fourth order are used in practice.

First Order Statistics → Mean, median, mode, minimum, maximum, percentiles
Describe the central or average value of data

Second Order Statistics → Variance, standard deviation, range, IQR, covariance, correlation, covariance matrix, eigenvalues, eigenvectors
Describe spread, relationships, and main directions of variance in data

Third Order Statistics → Skewness, third central moment
Describe data asymmetry (left or right tilt)

Fourth Order Statistics → Kurtosis, excess kurtosis, fourth central moment
Describe tail heaviness and extreme values


## **Linear Algebra → Vector Operations → Bilinear Products**

**Dot Product (Inner Product)**

Combines two vectors → single number (scalar), Measures how similar or aligned two vectors are:-

a · b = |a||b|cos(θ)

Used for similarity, projection, angle, and work in physics. 

(measuring similarity between two text documents in search engines; result is a single number, range = −|a||b| to +|a||b|; limitation: loses detailed feature-level information.). 

i. BERT4Rec → Uses dot product inside self-attention (query · key)

ii. SASRec / SAS4Rec → Uses dot product in self-attention for sequence modeling

Example 1:-

Dot Product (2×1 · 2×1)

Let a = [1, 2]  
Let b = [3, 4]

Dot product:
a · b = (1 × 3) + (2 × 4)
      = 3 + 8
      = 11   (scalar)


**Outer Product**

Combines two vectors → matrix. Shows all pairwise interactions between elements

a ⊗ b = a bᵀ

Used in covariance matrices, PCA, machine learning. 

(Outer Product → building a covariance matrix from data in finance or ML; result is a matrix with no fixed range; limitation: creates large matrices and is computationally expensive.)

iii. xLSTM → Uses outer product–style interactions to capture higher-order feature relationships.

Some advanced memory and interaction modules inside xLSTM rely on matrix-form interactions, not just scalars.

Example 2:-

Outer Product (2×1 ⊗ 1×2)

a ⊗ b = a bᵀ

a = [1
     2]

bᵀ = [3  4]

Outer product:
[1] [3  4] = [1×3  1×4] = [3  4]
[2]         [2×3  2×4]   [6  8]


## Linear Algebra → Matrix Theory / Linear Transformations

Eigenvector:- Special direction that remains unchanged in direction when a linear transformation is applied. Represents a fundamental pattern or axis along which the system behaves consistently.

Eigenvalue:- Scalar that measures how strongly a transformation acts along its corresponding eigenvector. Iindicates the magnitude of scaling or importance of that direction.
