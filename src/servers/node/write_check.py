
def blind_wr(write_request, p, param, pub):
    wr = [write_request[i] for i in p]
    (G,g,h,o) = params
    k=o.random()
    for value in wr:
         value = k
