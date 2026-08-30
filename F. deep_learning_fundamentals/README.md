**List of Time Series Models:**
				
![image](https://github.com/user-attachments/assets/ab1386a7-c571-43ab-aa98-3ed0905c4d73)

**Latest MoR vs Transformer:**

<img width="1508" height="488" alt="image" src="https://github.com/user-attachments/assets/c3dea711-29e5-4f44-97a7-8964b9bfa4a1" />


**CNN Model Architectures:**

<img width="1717" height="443" alt="image" src="https://github.com/user-attachments/assets/699665f6-157a-434f-8ab5-f8bdc00718ab" />

--------------------------------------------

**Backpropagation Technique:**

![image](https://github.com/user-attachments/assets/01b02ad8-b838-4d5e-974c-730a27fa9532)

--------------------------------------------


**Case Study 1: Multi-Variable Time Series Analysis**   

Numerous large-scale projects and prominent financial institutions focus
 on predicting financial markets using advanced Artificial Intelligence (AI) and
 Machine Learning (ML) approach, leading to publicly available stock indices data
 sets. In this report, we will model, integrate the financial market movements using
 probabilistic graphical model approach and will incorporate economic indicators
 using external factors.
 
 This probabilistic approach incorporating a wide range of external factors that
 influence market behavior, such as macroeconomic trends, economic indicators,
 geopolitical events, technical indicators, regional and sector-specific develop
ments.

**Data Sources and Collection: ** 
Data used in this project were collected mainly from yahoo finance and government open source platforms. 

Major 7 indices  were considered in this study in three different regions such  as US, Europe and Asia. We use python API which will pull  historical data from yahoo finance (Indices data) and world  bank (wbdata for economic indicators) and store it in google  cloud for model development.

 Some of major indices were considers such as:
 
 • SP 500 (Standard and Poor’s 500)– USA: 500  of the largest publicly traded companies in the United States.
 
 • DowJones Industrial Average (DJIA)– USA: Includes 30  major, large-cap companies.
 
 • NASDAQComposite– USA: 3,000  companies listed on the NASDAQ Stock Market.
 
 • FTSE 100 (Financial Times Stock Exchange 100 Index) UK:  100 largest companies listed on the London Stock Exchange.
 
 • Nikkei 225– Japan: 225 blue-chip companies listed on the Tokyo Stock Exchange.
 
 • DAX(Deutscher Aktienindex)– Germany: It tracks 40 of the largest and most liquid companies on the Frankfurt Stock  Exchange.
 
 • Sensex (Sensitive Index)– India: Sensex tracks 30 well established and financially sound companies listed on the  Bombay Stock Exchange.


** Model Approach:**
1. Data Collection, (Yahoo finance for exploratory purpose)
2. Data Preprocessing,
3. Feature Engineering, (Functions to create 15 different technical indicators to evaluate the stocks)
4. Model Selection (Time series models)
5. Evaluation Metrics (Mean Square Error (MSE), Mean Absolute Error (MAE))
6. Results Interpretation And Visualization

![image](https://github.com/user-attachments/assets/c51eb893-0558-47f0-b4a7-98261db5507e)

----------------------------------------------------

**Case Study 2: Smart Buildings & Smart Cities Analytics:**

City List: Created a list of 20 major cities with their latitude and longitude coordinates.

Loop through Cities: The For loop goes through each city and calls get_weather_open_meteo, passing the latitude, longitude, and city name. 

Prediction: Time series foundational models would be utilized.

** Model Approach:**
1. Data Collection, (Major Weather Platforms API's),
        Example APIs for real-time environmental data:
	A. OpenWeatherMap (Temperature, humidity, wind, air quality) → https://openweathermap.org/api
	
	B. AirVisual API (CO2, PM2.5, Air Quality Index) → https://www.iqair.com/
	
	C. SmartThings API (IoT device integration) → https://smartthings.developer.samsung.com/
	
	D. **Google's SMart Buildings:** https://www.tensorflow.org/datasets/catalog/smart_buildings
	
	E. **CU-BEMS, smart building energy and IAQ data** [https://www.tensorflow.org/datasets/catalog/smart_buildings](https://www.kaggle.com/datasets/claytonmiller/cubems-smart-building-energy-and-iaq-data)
		
	F. Smart Cities: https://www.kaggle.com/datasets/magdamonteiro/smart-cities-index-datasets/data

	G. **Open Buildings:** https://sites.research.google/gr/open-buildings/

	H. **Smart Building Simulators:** https://github.com/google/sbsim

	I. Plus Code: https://maps.google.com/pluscodes/


3. Data Preprocessing
   
   A. Missing Data Handling: Simple averaging, forward fill (windows lead), backward fill (windows lag), mean/average.
   
4. Feature Engineering, (Functions to create/select different variables like Temperature, Humidity, CO2, PM2.5, VOCs, Noise, wind speed, carbon emissions, Oxygen, Light Levels, Air flow, thermal, vibrations and lot more.,)
5. Model Selection,
   A. Weights Normalization, standardizations.(Min-Max Scalling, z-Scoring etc.,)

![image](https://github.com/user-attachments/assets/269f508b-9207-42a1-80eb-fc5e7b1deb26)

6. Evaluation Metrics (Mean Square Error, etc), and
7. Results Interpretation


**Potential Advantages or Benefits Estimation for Smart Buildings:**

A. Predictive Maintenance = No Breakdowns, (Labor cost, Travel cost, Planned Visits) | B. Environmental Impact | C. Higher Asset Value | D. Carbon Emission, Energy Optimization and Savings | E. Integration with Renewable energy | F. Smarter Construction, Reduced Operational Waste, and Energy Efficient Buildings | G. Cleaner Indoor Air = Healthier Humans | H. Lower Utility Bills = Instant Payback | I. Carbon Taxes or Regulations | J. Talents, or workforce to a modern buildings | K. Operational Efficiency Without More Staff | L. Better ROI Over Time (Better resale value) | M. AI climate models, part of smart cities. I.e. Integration | N. Grid Independence & Energy Resilience (I.e During Grid Downtimes due to natural disasters, energy downtime etc.,) | O. Investing for Future Buildings

**General Value Prop:** Smart Buildings transform spaces into intelligent, responsive environments — cutting energy waste, boosting occupant comfort, and insights for better decisions — all while reducing carbon emissions and operating costs.

According to the IEA, **buildings are responsible for nearly 30-40% of global energy-related CO₂ emissions**. That’s Massive. Climate Change!


-------------------------------------------------------

**Case Study 3: AlphaFold Model Versions**

AlphaFold developed by DeepMind that predicts the 3D structure of proteins from their amino acid sequence with high accuracy. 

At its core, AlphaFold solves the "protein folding problem":

<img width="1213" height="286" alt="image" src="https://github.com/user-attachments/assets/cc944859-fd56-45a1-9eaf-d67247604010" />

We can reuse datasets across AlphaFold versions for single-sequence structure prediction, but only AlphaFold 2 is practically and fully usable today. AlphaFold 3 offers advanced capabilities, but access is restricted and not reproducible locally.

Version-Specific Considerations

AlphaFold 1
		A. Input format: FASTA + preprocessed MSAs (custom pipeline), Output: Distance maps + coordinate models via Rosetta
		B. Run locally: No official release; re-implementations exist but outdated
		C. Best use: **Academic comparison only (use as a baseline)**
		D. Can reuse sequences, but need to reconstruct old-style pipelines with multiple tools.

AlphaFold 2
		A. Input: FASTA, MSA generated via tools like JackHMMer, HHblits
		B. Output: 3D atomic coordinates (.pdb), confidence metrics (pLDDT)
		C. Run locally: Yes – full open-source model + Docker container available
		D. Best use: All structure prediction tasks; high-quality general model
		E. Same datasets work easily here with minimal adaptation.

AlphaFold 3
		A. Input: Protein + ligands/RNA/DNA (structured prompt)
		B. Model availability: NOT open-source – only accessible via DeepMind’s API through Isomorphic Labs / Helix
		C. Output: 3D structures with complex components (protein-ligand, etc.)
		D. Best use: Modeling complexes and interactions (not just single proteins)

Exploration Datasets:

<img width="797" height="200" alt="image" src="https://github.com/user-attachments/assets/adeb2b2a-af15-4d9b-be75-47337f820446" />

Applications:

		A. Protein structure prediction: AlphaFold revolutionized prediction of 3D protein structures from sequences with near-experimental accuracy.
		B. Drug discovery: Used to model target proteins for virtual screening, docking, and rational drug design.
		C. Protein–protein interaction modeling: AlphaFold-Multimer helps predict how proteins bind and form complexes.
		D. Functional annotation of unknown proteins: Enables structural insights for "dark proteome" in genomics and metagenomics.
		E. Studying disease mutations: Helps analyze structural effects of mutations in cancer, neurodegeneration, and other conditions.


Few Other Data Apps and For MLops Experiements:

1.https://www.tensorflow.org/tensorboard
2. https://grafana.com/
3. https://streamlit.io/
4. https://wandb.ai/


Top 8 frameworks for AI agent development:

		A. LangChain – LLM-based agents with tools, memory, and chains
		B. AutoGen (Microsoft) – Multi-agent orchestration and conversation with tool use
		C. OpenAI Gym / Gymnasium – Standard RL environments for training agents
		D. Hugging Face Transformers + Agents – Pretrained LLMs with built-in tools and agent API
		E. Unity ML-Agents Toolkit – 3D simulation and training for embodied/robotic agents
		F. Haystack (deepset) – Retrieval-Augmented Generation (RAG) pipelines for knowledge agents
		G. RLlib (Ray) – Scalable reinforcement learning, supports multi-agent training
		H. CrewAI – LLM-based agent teamwork with role delegation and task collaboration



 



