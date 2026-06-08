import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	OCRTool,
	FileReadTool
)






@CrewBase
class ProcurementAuditorAiCrew:
    """ProcurementAuditorAi crew"""

    
    @agent
    def invoice_processing_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["invoice_processing_specialist"],
            
            
            tools=[				OCRTool(),
				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def compliance_auditor(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["compliance_auditor"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def risk_assessment_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["risk_assessment_analyst"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def audit_report_generator(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["audit_report_generator"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def process_invoice_documents(self) -> Task:
        return Task(
            config=self.tasks_config["process_invoice_documents"],
            markdown=False,
            
            
        )
    
    @task
    def compliance_verification(self) -> Task:
        return Task(
            config=self.tasks_config["compliance_verification"],
            markdown=False,
            
            
        )
    
    @task
    def risk_assessment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["risk_assessment_analysis"],
            markdown=False,
            
            
        )
    
    @task
    def generate_comprehensive_audit_report(self) -> Task:
        return Task(
            config=self.tasks_config["generate_comprehensive_audit_report"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ProcurementAuditorAi crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


