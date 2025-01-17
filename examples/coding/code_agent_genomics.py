from pathlib import Path
from dotenv import load_dotenv
from llm_sandbox.micromamba import MicromambaSession
from llm_sandbox.docker import SandboxDockerSession

from just_agents.interfaces.IAgent import build_agent, IAgent
from just_agents.llm_session import LLMSession
from examples.coding.tools import write_thoughts_and_results
from examples.coding.mounts import input_dir, output_dir, coding_examples_dir

load_dotenv(override=True)

if __name__ == "__main__":
    assistant: LLMSession= build_agent(coding_examples_dir / "code_agent.yaml")
    result, thoughts = assistant.query("Analyze vcf file with human genome using vcflib python binding."
                                       "Extract an overall number of SNPs, deletions, and insertions. Show SNPs distribution over chromosomes."
                                       "On this URL you will find vcf file for this task 'https://drive.usercontent.google.com/download?id=13tPNQsVXMtQKFcTeTOZ-bi7QWa9OdPD4'."
                                       " Save results as genomic_result.txt")
    write_thoughts_and_results("genomics", thoughts, result)