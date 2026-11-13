import math
#be able to calculate different physics calculators, inputing value and checkmarking which ones
#the person wants to calculate (front end and backend)
#idea: (wave speed and of sound, wavelength
#frequency, speed in temperature,
# and latent vap and transform,)
#voltage, resistance and current, tot voltage, resistance and current, and cost of electricity watts

#make it so you can pick multiple number from 1 to ... and that decides which calculators you
#are gonna use, if you dont have values for one it says you wont be able to use it
# so if 1 is velocity and 2 is acceleration, then 2 can use values from 1, unless you just picked
# 2 and give values, make so that if you have values for velocity but not for acceleration,
# you can pick an option that uses values from velocity
#start:

#main: different unit linkes, but checkbox, once click it pops up enter values, everything that is checkboxed
#and has values will return output


#kinematics and forces
#velocity
def vel(v, d, t):
    res_v = d/t
    res_t = d/v
    res_d = v*t
    res = [res_d, res_v, res_t ]
    return res
#acceleration
def acc(a, v, t):
    res_a = v/t
    res_t = v/a
    res_v = a*t
    res = [res_a, res_v, res_t ]
    return res

#force is mass times acceleration
def force(f, m, a):
    res_a = f/m
    res_m = f/a
    res_f = m*a
    res = [res_f, res_m, res_a ]
    return res

#quadratic
def quad(a, b, c):
    D = b**2 - 4*a*c
    
    if D < 0:
        return "No real roots"
    elif D == 0:
        x = -b / (2*a)
        return f"One real root: x = {x}"
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        return f"Two real roots: x1 = {x1}, x2 = {x2}"
    
    def at_a_height_no_angle():
        return 
    def at_a_flat_with_angle():
        return
    def at_a_height_with_angle():
        return 
    def pulley_que():
        return
    #friction coefficients and projectile 5 eq

    #work
#work
def force(w, f, d):
    res_d = w/f
    res_f = w/d
    res_w = f*d
    res = [res_w, res_f, res_d ]
    return res
#potential energy
def pe(m, h):
    res = (m*(9.8)*h)
    return res 
#kinetic energy
def ke(m, v):
    res = (m*(v^2))/2
    return res
#conservation
def conservation(h):
    res = math.sqrt(2*(9.8)*h)
    return res
#power
def power(p, E, t):
    res_p = E/t
    res_t = p/E
    res_E = p*t
    res = [res_p, res_t, res_E]
    return res
#efficiency
def efficiency(e, i, o):
    res_e = (o/i)*100
    res_i = (o/e)*100
    res_o = (i*e)/100
    res = [res_e, res_i, res_o]
    return res
#calories burned
def cals(f, d):
    res_w = f*d
    res_cals = res_w/4186
    return res_cals+" calories"
#mct
def mct(q, m, c, t_1, t_2, t_1k, t_2k):
    #get to choose the thing for the different heat capacity "c"
    while not t_1 and t_2:
        t_2 = t_2k-273
        t_1 = t_1k-273

    res_q = m*c*(t_2-t_1)
    res_m = q/(c*(t_2-t_1))
    res_c = q/(m*(t_2-t_1))
    res_t_1 = (q/(m*c))-t_2
    res_t_2 = (q/(m*c))+t_1
    res_kelvin_1 = res_t_1+273
    res_kelvin_2 = res_t_2+273
    res = [res_q, res_m, res_c, res_t_1 + f" = kelvin: {res_kelvin_1}", res_t_2 + f" = kelvin: {res_kelvin_2}"]
    return res


    #waves
#wave speed
def waveSpeed(v, f, l):
    res_v = f*l
    res_f = v/l
    res_l = v/f
    res = [res_v, res_f, res_l]
    return res

    #electromagnetism
def vol_diff(v, i, r):
    res_v = i*r
    res_i = v/r
    res_r = v/i
    res = [res_v, res_i, res_r]
    return res

def series(series_input):
    tot_series = [series_v, series_i, series_r+"\n"]
    for i in range(series_input):
        series_v = int(input("Voltage: "))
        series_i = int(input("current: "))
        series_r = int(input("resistance: "))
    return
def parrallel():
    return
def mixed_circ():
    return
    #v,r,i also say like parralel: and series: which can calculate


v = int(input(":"))
t = int(input(":"))
d = int(input(":"))
print(vel(v,d,t))


