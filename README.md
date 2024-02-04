<div style="text-align: center;">
  <img src="images/iquhack.png" alt="drawing" width="150"/>
</div>

# Quantum Generative Adversarial Networks (QGANs) with Quandela's Perceval

---

Quandela Challenge - Team 5 (BiQer Mice from Mars) Members: [Dhanvi Bharadwaj](https://github.com/d-bharadwaj/), [Kshitij Duraphe](https://github.com/ksd3/), [Nico Salm](https://github.com/nicosalm/), [Sarannya Bhattacharya](https://github.com/Emperor963/), [Vinay Swamik](https://github.com/vinayswamik/).

<div style="text-align: center;">
  <img src="images/bu.png" alt="drawing" width="100"/>
  <img src="images/uw.png" alt="drawing" width="200"/>
  <img src="images/quandela.png" alt="drawing" width="102"
  >
</div>

---

## Contents
- [Quantum Generative Adversarial Networks (QGANs) with Quandela's Perceval](#quantum-generative-adversarial-networks-qgans-with-quandelas-perceval)
  - [Contents](#contents)
  - [Theoretical Motivation](#theoretical-motivation)
  - [Step 1: Assembling our Perceval circuit from Figure 1.d](#step-1-assembling-our-perceval-circuit-from-figure-1d)
  - [Step 2: Generate Initial Quantum State](#step-2-generate-initial-quantum-state)
  - [Step 3: Train the Q-GAN](#step-3-train-the-q-gan)
  - [A comparison of approaches](#a-comparison-of-approaches)
  - [Bonus no. 1!](#bonus-no-1)
  - [Bonus no. 2!](#bonus-no-2)
  - [Bonus no. 3!](#bonus-no-3)
  - [Graphs](#graphs)
  - [Results](#results)
  - [Sources](#sources)
  - [Acknowledgments](#acknowledgments)

## Theoretical Motivation

QGANs represent the convergence of quantum computing and machine learning, offering novel possibilities for quantum state generation Demonstrating in partnership with [Quandela](https://www.quandela.com/)'s [Perceval](https://perceval.quandela.net/) framework, we work to leverage QGANs to capitalize on photon advantage. This implementation showcases precise quantum state control, vital for quantum computing applications. It connects theoretical research with practical experimentation, aiding quantum machine learning and [quantum photonics](https://en.wikipedia.org/wiki/Integrated_quantum_photonics) practitioners.

In summary, this work showcases QGANs' practicality in quantum photonics, advances quantum state engineering, and serves as a foundation for future quantum machine learning research, bridging theory with real-world applications.

## Step 1: Assembling our Perceval circuit from Figure 1.d
First things first! – We assemble our circuit. We are given GANs as a learning architecture and must describe a bi-ququartite circuit using Perceval as described in [1].  

<div style="text-align: center;">
  <img src="images/circuit.png" alt="drawing" width=""/>
</div>

In particular, we build and pit a Generator against a Discriminator against one another, in an attempt to approach a Nash equilibrium. We compose these two components as our "chip".

<div style="text-align: center;">
  <img src="images/gan.png" alt="drawing" width=""/>
</div>

<small>(a – d), [1]</small>

## Step 2: Generate Initial Quantum State

It is important to note that we must toss aside our understanding of the traditional Qubit when working with quantum photonics. 

## Step 3: Train the Q-GAN



## A comparison of approaches

## Bonus no. 1!

## Bonus no. 2!

## Bonus no. 3!

## Graphs

## Results

## Sources

1. [Quantum generative adversarial learning in photonics](https://arxiv.org/pdf/2310.00585.pdf) [Paper]

2. [Information about Quandela's iQuHack2024 challenge](https://github.com/iQuHACK/2024_Quandela) [Challenge repo]

3. [Quandela Perceval framework](https://perceval.quandela.net/)

## Acknowledgments

***A special thanks to everyone on the Quandela team for their support!***