import numpy as np

def transfer_and_attend(X, W_q_lin, W_k_lin, W_v_lin):
    """
    Transfer linear-style weights (shape (d_out, d_in)) into parameter-style
    weights (shape (d_in, d_out)) and compute single-head causal self-attention.

    Args:
        X: input array of shape (seq_len, d_in)
        W_q_lin, W_k_lin, W_v_lin: linear-style weight matrices of shape (d_out, d_in)

    Returns:
        Nested list of shape (seq_len, d_out): the self-attention output.
    """
    X = np.array(X)
    W_q_lin = np.array(W_q_lin)
    W_k_lin = np.array(W_k_lin)
    W_v_lin = np.array(W_v_lin)
    W_q = W_q_lin.T
    W_k = W_k_lin.T
    W_v = W_v_lin.T
    
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    
    seq_len, d_k = Q.shape
    scores = (Q @ K.T) / np.sqrt(d_k)
    mask = np.triu(np.ones((seq_len, seq_len), dtype=bool), k=1)
    scores[mask] = -np.inf
    scores -= np.max(scores, axis=-1, keepdims=True)
    exp_scores = np.exp(scores)
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    output = attention_weights @ V
    return output.tolist()