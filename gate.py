def and_gate(x1,x2):
    w0 = -0.5
    w1 = 0.5
    w2 = 0.5
    threshold = 0.0
    s = w0 +(w1*x1)+(w2*x2)
    if s >= threshold:
        result = 1
    else:
        result = 0
        
    print('output y={} [s={}]'.format(result,s))
        
and_gate(0,0)
and_gate(0,1)
and_gate(1,0)
and_gate(1,1)