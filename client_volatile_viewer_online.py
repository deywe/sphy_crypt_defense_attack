# -*- coding: utf-8 -*-
from ursina import *
import requests
import threading
import sys
import numpy as np

# --- PRODUCTION NETWORK CONFIGURATION (ORACLE CLOUD VM) ---
SERVER_URL = "http://161.153.0.202:2002"  
SESSÃO_TOKEN = None
CONEXAO_ESTAVEL = True
BUFFER_MEMORIA_VOLATIL = None

# --- SPHY PHYSICAL SIMULATION ENGINE ---
class SPHYUrsinaEngine:
    def __init__(self):
        self.num_qubits = 120
        self.phi = (1.0 + np.sqrt(5.0)) / 2.0
        self.clock = 0.0
        self.status = "STABLE_RESONANCE_ENGAGED"
        
        # Quantum Invariants & Field Simulation
        self.coherence = 1.0
        self.shannon_entropy = 0.0
        self.bohm_pressure_max = 0.0
        self.landauer_dissipation_pw = 0.0
        self.delta_g = 0.0  # Gravitational metric variance (Delta g)
        
        self.escala_ataque_s = 1.0
        self.attack_wave = 0.0
        self.shield_activation = 0.0
        
        self.theta = np.linspace(0, 2 * np.pi, self.num_qubits)
        self.vertices_3d = []

    def recalibrar_tensores(self):
        self.theta = np.linspace(0, 2 * np.pi, self.num_qubits)

    def processar_dinamica(self):
        self.clock += 0.03
        gatilho_ciclico = np.sin(self.clock * 0.4)
        
        # Automated Attack Engine
        if gatilho_ciclico > 0.4:
            frequencia_intrusa = (1.0 / (self.phi ** 2)) + (0.25 * self.escala_ataque_s) + np.sin(self.clock * 2.0) * 0.2
        else:
            frequencia_intrusa = (1.0 / (self.phi ** 2))
            
        delta_fase = np.abs(frequencia_intrusa - (1.0 / (self.phi ** 2)))
        self.coherence = 1.0 / (1.0 + delta_fase)
        
        if self.coherence < 0.85:
            self.status = "ATTACK_MUTED_BY_COHERENCE_SHIELD"
            amplitude_choque = 15.0 * self.escala_ataque_s  
            self.attack_wave = lerp(self.attack_wave, np.sin(self.clock * 6.0) * amplitude_choque, 0.2)
            self.shield_activation = lerp(self.shield_activation, 1.0, 0.08)
        else:
            self.status = "STABLE_RESONANCE_ENGAGED"
            self.attack_wave = lerp(self.attack_wave, 0.0, 0.1)
            self.shield_activation = lerp(self.shield_activation, 0.0, 0.08)

        # 1. Metric: Shannon Entropy
        counts, _ = np.histogram(self.theta, bins=20, range=(0, 2*np.pi))
        p = counts / self.num_qubits
        p = p[p > 0]
        self.shannon_entropy = -np.sum(p * np.log2(p))

        # 3.0D String Mesh Reconstruction
        self.vertices_3d = []
        r_atual = np.zeros(self.num_qubits)
        
        for i in range(self.num_qubits):
            progresso = i / self.num_qubits
            raio_base = 8.0 + (1.5 - 8.0) * progresso
            
            if self.status == "STABLE_RESONANCE_ENGAGED":
                r_atual[i] = raio_base + np.sin(self.clock + i * 0.1) * 0.2
                self.theta[i] = (self.theta[i] + 0.01 * self.phi) % (2 * np.pi)
                z = -5.0 + (5.0 - (-5.0)) * progresso
            else:
                fator_borda = (1.0 - progresso)
                ruido = np.random.normal(0, 0.2 * self.escala_ataque_s) * self.shield_activation * fator_borda
                r_atual[i] = raio_base + (self.attack_wave * 0.1 * fator_borda) + ruido
                
                z_base = -5.0 + (5.0 - (-5.0)) * progresso
                z = z_base + (self.attack_wave * 0.05 * fator_borda)
                self.theta[i] = (self.theta[i] + 0.01 * self.phi + (self.attack_wave * 0.001 * fator_borda)) % (2 * np.pi)

            x = r_atual[i] * np.cos(self.theta[i])
            y = r_atual[i] * np.sin(self.theta[i])
            self.vertices_3d.append(Vec3(x, y, z))

        # 2. Metric: Bohm Quantum Pressure
        grad_r = np.gradient(r_atual)
        self.bohm_pressure_max = np.max(np.abs(np.gradient(grad_r))) * 10
        
        # 3. Metric: Gravitational Metric Tensor Variance
        if self.status != "STABLE_RESONANCE_ENGAGED":
            self.delta_g = np.var(r_atual) * 9.80665 * self.escala_ataque_s
        else:
            self.delta_g = lerp(self.delta_g, 0.0000, 0.1) 

        # 4. Metric: Landauer Dissipation Bound
        k_b = 1.380649e-23
        if self.status != "STABLE_RESONANCE_ENGAGED":
            self.landauer_dissipation_pw = (self.shannon_entropy * k_b * 293.15 * np.log(2) * 1e21) * self.escala_ataque_s
        else:
            self.landauer_dissipation_pw = lerp(self.landauer_dissipation_pw, 0.01, 0.1)

sphy_sim = SPHYUrsinaEngine()

# --- GRAPHICS ENGINE SETUP ---
app = Ursina(development_mode=False, borderless=False) 
window.title = "SPHY COGNITIVE ORACLE: URSINA EXTREME MATRIX"
window.size = (1280, 720)
window.color = color.black

window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False

# 3D Filament Entity Configuration
corda_quantum = Entity(
    model=Mesh(vertices=sphy_sim.vertices_3d, mode='line', thickness=2), 
    color=color.cyan,
    position=(2.5, -1, 0) 
)

camera.position = (0, 6, -16)
camera.rotation_x = 22

# --- TELEMETRY HUD LAYOUT ---
hud_bg = Entity(
    parent=camera.ui,
    model='quad',
    scale=(0.42, 0.9),
    position=(-0.65, 0),
    color=color.rgba(0.05, 0.06, 0.11, 0.94),  
    z=1  
)

txt_titulo = Text(text="SPHY COGNITIVE TELEMETRY", position=(-0.82, 0.4), scale=1.4, color=color.white)
txt_sub = Text(text="Black Swan Research // Harpia OS", position=(-0.82, 0.36), scale=0.9, color=color.gray)

txt_monitor_label = Text(text="OPERATIONAL SYSTEM MONITOR:", position=(-0.82, 0.28), scale=1.0, color=color.light_gray)
status_panel = Entity(parent=camera.ui, model='quad', scale=(0.36, 0.05), position=(-0.65, 0.22), color=color.cyan)
status_text = Text(text="DYNAMIC HOMEOSTASIS ENGAGED", position=(-0.81, 0.23), scale=1.0, color=color.black)

txt_coherence = Text(text="Phase Coherence: 100.00%", position=(-0.82, 0.14), scale=1.0, color=color.white)
txt_entropy = Text(text="Shannon Entropy (H): 0.0000 bits", position=(-0.82, 0.10), scale=1.0, color=color.white)
txt_bohm = Text(text="Bohm Pressure (Q): 0.00 eV", position=(-0.82, 0.06), scale=1.0, color=color.white)
txt_gravity = Text(text="Delta G (Δg): 0.0000 m/s²", position=(-0.82, 0.02), scale=1.0, color=color.orange)
txt_landauer = Text(text="Landauer Dissipation: 0.0000 pW", position=(-0.82, -0.02), scale=1.0, color=color.white)
txt_qubits = Text(text="Tracked Qubits: 120 | Chaos Power: 1.0x", position=(-0.82, -0.06), scale=1.0, color=color.white)

# Coherence Progress Bar
barra_bg = Entity(parent=camera.ui, model='quad', scale=(0.36, 0.015), position=(-0.65, -0.11), color=color.dark_gray)
barra_coher = Entity(parent=camera.ui, model='quad', scale=(0.36, 0.015), position=(-0.65, -0.11), color=color.cyan, origin_x=-0.5)

txt_commands = Text(text="COMMANDS: [UP/DN] Scale Qubits  ||  [S] Inject Chaos", position=(-0.82, -0.2), scale=0.9, color=color.gold)
txt_ram = Text(text="Volatile RAM Allocation: Active", position=(-0.82, -0.28), scale=0.8, color=color.green)
txt_token = Text(text="Vacuum Session Token: Locked", position=(-0.82, -0.31), scale=0.8, color=color.gray)

# --- HARDWARE RUNTIME UPDATE LOOP ---
def update():
    global CONEXAO_ESTAVEL
    
    # Strict Online Enforcement Check
    if not CONEXAO_ESTAVEL:
        autodestruicao_memoria()

    if held_keys['up arrow']:
        if sphy_sim.num_qubits < 1200:
            sphy_sim.num_qubits += 10
            sphy_sim.recalibrar_tensores()
    elif held_keys['down arrow'] and sphy_sim.num_qubits > 20:
        sphy_sim.num_qubits -= 10
        sphy_sim.recalibrar_tensores()

    sphy_sim.processar_dinamica()
    
    # Direct VRAM Buffer Streaming
    corda_quantum.model.vertices = sphy_sim.vertices_3d
    corda_quantum.model.generate() 
    
    corda_quantum.rotation_z += 0.25
    corda_quantum.rotation_y = np.sin(sphy_sim.clock * 0.2) * 10
    
    # Real-Time HUD Synchronization
    txt_coherence.text = f"Phase Coherence: {sphy_sim.coherence * 100:.2f}%"
    txt_entropy.text = f"Shannon Entropy (H): {sphy_sim.shannon_entropy:.4f} bits"
    txt_bohm.text = f"Bohm Pressure (Q): {sphy_sim.bohm_pressure_max:.2f} eV"
    txt_gravity.text = f"Delta G (Δg): {sphy_sim.delta_g:.4f} m/s²"
    txt_landauer.text = f"Landauer Dissipation: {sphy_sim.landauer_dissipation_pw:.4f} pW"
    txt_qubits.text = f"Tracked Qubits: {sphy_sim.num_qubits} | Chaos Power: {sphy_sim.escala_ataque_s:.1f}x"
    
    barra_coher.scale_x = 0.36 * min(sphy_sim.coherence, 1.0)
    
    if sphy_sim.status == "STABLE_RESONANCE_ENGAGED":
        status_panel.color = color.cyan
        status_text.text = "DYNAMIC HOMEOSTASIS ENGAGED"
        status_text.color = color.black
        corda_quantum.color = color.cyan
        barra_coher.color = color.cyan
    else:
        status_panel.color = color.red
        status_text.text = "ACTIVE COHERENCE SHIELD FILTER"
        status_text.color = color.white
        corda_quantum.color = color.red
        barra_coher.color = color.orange

    if BUFFER_MEMORIA_VOLATIL:
        txt_ram.text = f"Volatile RAM Bound: {len(BUFFER_MEMORIA_VOLATIL)} Bytes"
        txt_token.text = f"Vacuum Token: {SESSÃO_TOKEN[:24]}..."

# --- KEYBOARD INPUT INTERCEPTOR ---
def input(key):
    if key in ('up arrow', 'arrow up'):
        if sphy_sim.num_qubits < 1200:
            sphy_sim.num_qubits += 10
            sphy_sim.recalibrar_tensores()
            print(f"[URSINA] Qubits scaled up to: {sphy_sim.num_qubits}")
    elif key in ('down arrow', 'arrow down'):
        if sphy_sim.num_qubits > 20:
            sphy_sim.num_qubits -= 10
            sphy_sim.recalibrar_tensores()
            print(f"[URSINA] Qubits scaled down to: {sphy_sim.num_qubits}")
    elif key == 's':
        if sphy_sim.escala_ataque_s < 5.0:
            sphy_sim.escala_ataque_s += 0.5

# --- PERSISTENT CORE HEALTH CHECK (HEARTBEAT) ---
def loop_heartbeat():
    global CONEXAO_ESTAVEL
    while CONEXAO_ESTAVEL:
        try:
            response = requests.post(f"{SERVER_URL}/ping?token={SESSÃO_TOKEN}", timeout=2)
            if response.status_code != 200:
                CONEXAO_ESTAVEL = False
                break
        except Exception:
            CONEXAO_ESTAVEL = False
            break
        time.sleep(1.0)

def autodestruicao_memoria():
    global BUFFER_MEMORIA_VOLATIL, CONEXAO_ESTAVEL
    print("\n💥 [SECURITY CORE TRIGGERED] Cloud connection lost. Flushing RAM buffers...")
    if BUFFER_MEMORIA_VOLATIL is not None:
        del BUFFER_MEMORIA_VOLATIL
    BUFFER_MEMORIA_VOLATIL = None
    CONEXAO_ESTAVEL = False
    print("🔒 Volatile memory sanitized. Pipeline closed.")
    sys.exit(0)

def iniciar_ambiente_efemero():
    global SESSÃO_TOKEN, CONEXAO_ESTAVEL, BUFFER_MEMORIA_VOLATIL
    print("🌐 Synchronizing with Oracle Cloud infrastructure (161.153.0.202)...")
    try:
        reg = requests.get(f"{SERVER_URL}/solicitar_conexao", timeout=3).json()
        SESSÃO_TOKEN = reg["token_acesso"]
        
        thread_ping = threading.Thread(target=loop_heartbeat, daemon=True)
        thread_ping.start()
        
        dados_stream = requests.get(f"{SERVER_URL}/obter_payload?token={SESSÃO_TOKEN}", timeout=3).json()
        BUFFER_MEMORIA_VOLATIL = bytes.fromhex(dados_stream["payload_bytes_hex"])
        print(f"[SUCCESS] Core validated and allocated in volatile memory.")
        
        app.run()

    except Exception as e:
        print(f"Critical infrastructure pipeline failure: {e}")
        autodestruicao_memoria()

if __name__ == "__main__":
    try:
        iniciar_ambiente_efemero()
    except KeyboardInterrupt:
        autodestruicao_memoria()