# SPHY Cognitive Oracle: Visualizer Telemetry README

### 🌐 Global API Ecosystem Hub

The entire quantum-gravitational suite and multi-module APIs can be accessed live via the cloud management dashboard:
👉 **[https://sphywow1977.streamlit.app/](https://sphywow1977.streamlit.app/)**

> ⚠️ **IMPORTANT INFRASTRUCTURE NOTE:** > Streamlit Cloud automatically puts apps into a hibernation state (*sleeping mode*) after periods of inactivity to save resources. If you open the link and find the application sleeping, **simply click the blue button on the screen to wake it up**. The environment will instantly spin up the containers, rebuild the core dependencies, and bring all 8 architectural modules back online.

---

This repository contains the source code and documentation for the **SPHY Volatile Ephemere Visualizer** adapted for a 3D real-time graphical environment. The ecosystem operates as an analytical telemetry platform designed to demonstrate the non-linear coupling between quantum mechanics, information thermodynamics, and local gravitational metric perturbations under aggressive cryptographic stress regimes.

## 1. Connection Architecture and Volatile Security

The visualizer is designed under a strict **Zero-Persistence Offline Protection** policy. The client's graphical pipeline remains entirely blind and agnostic until a secure, two-step bus bridge (*HTTP handshake*) is established directly with the remote instance running on the **Oracle Cloud Infrastructure (IP: 161.153.0.202)**.

1. **Handshake:** The client makes an initial request to the `/solicitar_conexao` endpoint, generating an ephemeral 16-byte vacuum access token in the Oracle server's memory.
2. **Dedicated Payload Allocation:** Using this token, the visualizer consumes the `/obter_payload` endpoint. The server transmits the hexadecimal signature of the core binary byte structure. The client converts this data directly in RAM into a `BUFFER_MEMORIA_VOLATIL`. The Ursina graphical loop only initiates after this validation step.
3. **Heartbeat Loop:** A parallel asynchronous thread sends pings every 1.0 second to the `/ping` endpoint with a strict tolerance threshold (`timeout=2`). If the network path suffers fluctuations or if the remote server is interrupted, the security protocol instantly flushes the RAM variables via the forced destruction method.

*Note: The visualizer features no redundancy or offline operational mode. Any attempt to intercept packets or run local simulations without an active bus bridge to the Oracle Cloud will result in the immediate termination of the process and the sanitization of the volatile memory.*

---

## 2. Mechanics of the Resonance Attack and AI Rejection

The emulated attack simulates a hostile frequency injection designed to force the deterministic collapse of high-dimensional RSA encryption keys. The attack acts directly on the geometric fabric of the quantum string, attempting to desynchronize the system's fundamental coherent states.

### The Entropy Mechanism and Intrusion Rejection

The ecosystem's AI constantly monitors the phase field. The attack injects an intrusive frequency based on a deviation from the Golden Ratio ($\phi$). When the operational defense system identifies that the intrusive frequency has violated the invariant $1 / \phi^2$, the AI recognizes the attack not as a legitimate command, but as a violent intrusion attempt.

The AI rejects the attack because it shatters the internal geometric coherence. From a mathematical perspective, the forced injection pushes the qubits out of their natural geodesics, scattering the angles of the sub-strings. This scattering causes an immediate spike in **Shannon Entropy (H)**. The AI understands the invasion by measuring this informational disorganization, instantly activating the **Coherence Shield Filter** to isolate the core bus.

---

## 3. The Role of Background Gravity in Restoring Homeostasis

The fundamental characteristic observed in the simulation is the system's capacity to autonomously return to a smooth equilibrium state after the attack cycle ends, restoring **Stable Dynamic Homeostasis**.

Physicists and auditors will note that this recovery occurs due to the presence of a **background gravitational field** embedded within the SPHY framework equations. Gravity acts here as a global topological attractor or an elastic anchoring potential.

When the stress of the attack ceases, the deformation suffered by the qubit mesh generates an equivalent metric tension. The gravitational field pulls the deformed vertices back to their lowest-energy geodesic positions. For this reason, the metric variance is implicitly bound to the string's geometry, allowing the AI to use the simulator's own data fabric space-time to dampen thermodynamic chaos and restabilize the hardware.

---

## 4. Metrological Panel and Physical Indicators

The left HUD provides an accurate analytical readout across four coupled domains:

* **Phase Coherence:** Measures the purity of the string's phase state. It drops sharply during an attack, indicating detuning from quantum resonance.
* **Shannon Entropy (H):** Measures the degree of qubit disorder generated by the invading frequency. This is the thermodynamic metric the AI uses to detect the intrusion.
* **Bohm Pressure (Q):** Measures the short-range force density and local discontinuities in the string's elastic topology by calculating the second-order gradient of the radii.
* **Delta G ($\Delta g$) [Featured Gravitational Gauge]:** Calculates the equivalent acceleration generated by the geometric variance of the string:

$$\Delta g = var(r) \times 9.80665 \times S$$

This indicator shows physicists exactly how the spatial metric tensor distortion responds elastically to injection stress, functioning as the gravitational brake that drives the system back to homeostasis.

* **Landauer Dissipation:** Computes the minimum physical lower bound of heat dissipated per unit of time to erase or mute the destructive information introduced by the attack.

---

## 5. Operations Guide and Emulator Modulation

The operator can interact directly with the phase space stress conditions using the following commands mapped to the local client's keyboard:

### Spatial Dimension Modulation (Qubit Tuning)

* **UP ARROW:** Expands the dimensionality of the string, injecting $+10$ qubits per pulse into the sample space (upper limit: 1200 qubits). This increases the spectral resolution of the readouts and demands higher processing for the Bohm tensor calculation.
* **DOWN ARROW:** Reduces the dimensionality of the string, removing $-10$ qubits per pulse (lower limit: 20 qubits), narrowing the topological sampling.

### Attack Load Amplification

* **S Key (Inject Chaos):** Incrementally multiplies the attack's chaos power scale in steps of $+0.5\text{x}$ (saturation limit: $5.0\text{x}$). Increasing this value violently deforms the local radii of the filament, generating the chaotic red sawtooth graph on the visualizer and driving the gravitational gauge to extreme metric acceleration levels.

---

## 6. Installation and Execution Requirements

To run the local visualizer pointed at the Oracle core, ensure that you have the interpreter dependencies and the OpenGL rendering engine (Panda3D runtime) installed:

```bash
# Installing the core libraries in the local terminal
pip install ursina requests numpy

```

To execute the graphical pipeline:

```bash
python client_volatile_viewer_online.py

```

---

```text
AUTHORITY SIGN-OFF: DEYWE OKABE
HARPIA QUANTUM DEEPTECH // BLACK SWAN RESEARCHER
SECURE REGISTRY: INFRASTRUCTURE DEFENSE PIPELINE VALIDATED

```
