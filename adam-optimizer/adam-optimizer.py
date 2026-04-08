import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here`
    param = np.array(param)
    grad = np.array(grad)
    m = np.array(m)
    v = np.array(v)
    mt = np.array(beta1*m + (1 - beta1) * grad)
    vt = np.array(beta2*v + (1 - beta2) * (grad**2))
    
    m_hat = np.array(mt / (1 - (beta1**t)))
    v_hat = np.array(vt / (1 - (beta2**t)))
    newParam = np.array(param - np.array(lr) * (m_hat / (np.sqrt(v_hat) + eps)))

    return newParam, mt, vt