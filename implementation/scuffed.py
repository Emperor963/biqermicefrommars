import perceval as pcvl
from perceval.components.unitary_components import PS, BS, PERM
import numpy as np
import random
import matplotlib.pyplot as plt
import torch
import torch.optim as optim

# ––– Circuit Implementation ––– # 

# We define two classes Generator and Discriminator, 
# and then pitch them against each other in a GAN.

        # self.n = n
        # self.gen_phi = [random.uniform(0, 2*np.pi) for _ in range(24)]
        # self.gen_theta = [random.uniform(0, 2*np.pi) for _ in range(20)]
        # self.gen_params = self.gen_phi + self.gen_theta
        # self.gen_params = torch.tensor(self.gen_params, requires_grad=True)
        # self.optimizer = optim.Adam([self.gen_params], lr=0.01)
        
 # define our generator class
class Generator:
 def __init__(self, n):
   self.n = n


 def create(self):
   qc = pcvl.Circuit(self.n, name = "Generator")
   qc.add(1, PS(phi=pcvl.P('gen_phi_1')))
   qc.add(2, PS(phi=pcvl.P('gen_phi_2')))
   qc.add(3, PS(phi=pcvl.P('gen_phi_3')))


   # mzi
   qc.add(0, BS(theta=pcvl.P('gen_theta_1'))).add(0, PS(phi=pcvl.P('gen_phi_4'))).add(0, BS(theta=pcvl.P('gen_theta_2')))
   qc.add(2, BS(theta=pcvl.P('gen_theta_3'))).add(2, PS(phi=pcvl.P('gen_phi_5'))).add(2, BS(theta=pcvl.P('gen_theta_4')))


   qc.add(1, PS(phi=pcvl.P('gen_phi_6')))
   qc.add(1, BS(theta=pcvl.P('gen_theta_5'))).add(1, PS(phi=pcvl.P('gen_phi_7'))).add(1, BS(theta=pcvl.P('gen_theta_6')))


   qc.add(0, BS(theta=pcvl.P('gen_theta_7'))).add(0, PS(phi=pcvl.P('gen_phi_8'))).add(0, BS(theta=pcvl.P('gen_theta_8')))
   qc.add(2, BS(theta=pcvl.P('gen_theta_9'))).add(2, PS(phi=pcvl.P('gen_phi_9'))).add(2, BS(theta=pcvl.P('gen_theta_10')))


   qc.add(0, PS(phi=pcvl.P('gen_phi_10')))
   qc.add(1, PS(phi=pcvl.P('gen_phi_11')))
   qc.add(2, PS(phi=pcvl.P('gen_phi_12')))


   # ----
   qc.add(1+4, PS(phi=pcvl.P('gen_phi_13')))
   qc.add(2+4, PS(phi=pcvl.P('gen_phi_14')))
   qc.add(3+4, PS(phi=pcvl.P('gen_phi_15')))


   # mzi
   qc.add(0+4, BS(theta=pcvl.P('gen_theta_11'))).add(0+4, PS(phi=pcvl.P('gen_phi_16'))).add(0+4, BS(theta=pcvl.P('gen_theta_12')))
   qc.add(2+4, BS(theta=pcvl.P('gen_theta_13'))).add(2+4, PS(phi=pcvl.P('gen_phi_17'))).add(2+4, BS(theta=pcvl.P('gen_theta_14')))


   qc.add(1+4, PS(phi=pcvl.P('gen_phi_18')))
   qc.add(1+4, BS(theta=pcvl.P('gen_theta_15'))).add(1+4, PS(phi=pcvl.P('gen_phi_19'))).add(1+4, BS(theta=pcvl.P('gen_theta_16')))


   qc.add(0+4, BS(theta=pcvl.P('gen_theta_17'))).add(0+4, PS(phi=pcvl.P('gen_phi_20'))).add(0+4, BS(theta=pcvl.P('gen_theta_18')))
   qc.add(2+4, BS(theta=pcvl.P('gen_theta_19'))).add(2+4, PS(phi=pcvl.P('gen_phi_21'))).add(2+4, BS(theta=pcvl.P('gen_theta_20')))


   qc.add(0+4, PS(phi=pcvl.P('gen_phi_22')))
   qc.add(1+4, PS(phi=pcvl.P('gen_phi_23')))
   qc.add(2+4, PS(phi=pcvl.P('gen_phi_24')))


   return qc


class Discriminator:
 def __init__(self, n):
   self.n = n


 def create(self):
   qc = pcvl.Circuit(self.n, name = "Discriminator")
   qc.add(0, PS(phi=pcvl.P('dis_phi_1')))
   qc.add(1, PS(phi=pcvl.P('dis_phi_2')))
   qc.add(2, PS(phi=pcvl.P('dis_phi_3')))


   # mzi
   qc.add(0, BS(theta=pcvl.P('dis_theta_1'))).add(0, PS(phi=pcvl.P('dis_phi_4'))).add(0, BS(theta=pcvl.P('dis_theta_2')))
   qc.add(2, BS(theta=pcvl.P('dis_theta_3'))).add(2, PS(phi=pcvl.P('dis_phi_5'))).add(2, BS(theta=pcvl.P('dis_theta_4')))


   qc.add(1, BS(theta=pcvl.P('dis_theta_5'))).add(1, PS(phi=pcvl.P('dis_phi_6'))).add(1, BS(theta=pcvl.P('dis_theta_6')))

   # ----


   qc.add(0+4, PS(phi=pcvl.P('dis_phi_7')))
   qc.add(1+4, PS(phi=pcvl.P('dis_phi_8')))
   qc.add(2+4, PS(phi=pcvl.P('dis_phi_9')))


   # mzi
   qc.add(0+4, BS(theta=pcvl.P('dis_theta_7'))).add(0+4, PS(phi=pcvl.P('dis_phi_10'))).add(0+4, BS(theta=pcvl.P('dis_theta_8')))
   qc.add(2+4, BS(theta=pcvl.P('dis_theta_9'))).add(2+4, PS(phi=pcvl.P('dis_phi_11'))).add(2+4, BS(theta=pcvl.P('dis_theta_10')))


   qc.add(1+4, BS(theta=pcvl.P('dis_theta_11'))).add(1+4, PS(phi=pcvl.P('dis_phi_12'))).add(1+4, BS(theta=pcvl.P('dis_theta_12')))


   return qc


gen = Generator(8).create()
dis = Discriminator(8).create()