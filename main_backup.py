from core.bharat_core import BharatCore
from perception.llm_wrapper import PerceptionEngine
from memory.chunked_memory import ChunkedMemory
from evolution.genetic_loop import GeneticEvolver
from rakshak.shield import RakshakShield

print("🇮🇳 BHARAT-AGI v0.1 Booting... 3026 Mindset Activated")

memory = ChunkedMemory(chunk_size=1000)
perception = PerceptionEngine()
shield = RakshakShield()
core = BharatCore(memory, perception, shield)
evolver = GeneticEvolver()

query = "Design a safer mine monitoring system for Jharkhand"
print(f"\n[USER]: {query}")

intent = perception.perceive(query)
print(f"[LAYER 2 PERCEPTION]: {intent}")

ethical = shield.ethical_check(query)
print(f"[LAYER 6 DHARMA]: {ethical}")

if ethical['allowed']:
    response = core.think(query, mode="innovator_researcher_scientist")
    print(f"\n[LAYER 3+7 RESPONSE]:\n{response}")
    evolver.evolve(response)

print("\n✅ Brick 1 Laid Successfully")
