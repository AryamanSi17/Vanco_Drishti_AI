# Vanco_Drishti_AI

# Drishti-360: Intelligent AI-Powered Safety Agent for Large Public Events


> **Transforming passive surveillance into proactive intelligence with 360° situational awareness at large-scale events.**

---

## Table of Contents

- [Overview](#overview)  
- [Motivation](#motivation)  
- [Key Features](#key-features)  
- [Architecture](#architecture)  
- [Technologies Used](#technologies-used)   
- [Demo](#demo)  
- [Impact](#impact)  
- [Future Work](#future-work)  

---

## Overview

Drishti-360 is an AI-powered real-time event surveillance platform designed to improve safety at large public gatherings by enabling proactive threat detection and crowd behavior analysis. Our system intelligently processes over 100 live CCTV feeds using advanced computer vision and cloud technologies, alerting control rooms proactively to potential incidents such as fires, stampedes, and panic.

---

## Motivation

Monitoring hundreds of live CCTV feeds manually is overwhelming and prone to visual fatigue, leading to delayed responses and potentially catastrophic outcomes. Drishti-360 automates surveillance, reducing operator workload by over 90%, while enhancing situational awareness and predictive safety measures.

---

## Key Features

- **Real-Time Object Detection:** Person, fire, smoke, and vehicle detection on 1000+ video feeds using Google Vertex AI Vision.  
- **Crowd Analytics:** Calculates relative crowd density, flow entropy, velocity, and bottleneck prediction.  
- **Intelligent Alerts:** Proactive notification of threats like fire outbreaks, crowd surges, and panic situations.  
- **Trajectory and Velocity Tracking:** Uses advanced Kalman filter based trackers for multi-person movement and velocity divergence analysis.  
- **Natural Language Querying:** Gemini-powered interface answers complex queries like “Which zone is at risk of stampede?”  
- **Scalable Cloud-Native Pipeline:** Lightweight numerical feature extraction and streaming to BigQuery for real-time and longitudinal analysis.  
- **Autonomous Drone Surveillance:** Drone dispatch for high-risk zones based on predictive analytics (future enhancement).  

---

## Architecture

![Architecture Diagram]()

- **Edge AI Devices:** Initial video input and object detection via Vertex AI Vision models.  
- **Cloud Data Lake:** Streamlined numerical data pipelines ingest and store feature-engineered signals in BigQuery.  
- **AI Agent (Gemini):** Uses LangChain for intelligent reasoning and natural language understanding over structured event data.  
- **Control Room Dashboard:** Firebase-powered UI for operators with real-time alerts and visualizations.  

---

## Technologies Used

- **Google Cloud Vertex AI Vision:** Real-time object detection  
- **Google Cloud BigQuery & Cloud Storage:** Scalable feature data storage & retrieval  
- **ultralytics & OpenCV:** Kalman filter and visualization for multi-person tracking  
- **Python & TensorFlow:** Core data processing and model integration  
- **Firebase Studio:** Dashboard and operator interface  
- **LangChain & Gemini Google vertex AI Agent :** Natural language understanding for querying data  

---
## demo

[firebase_url_drishti_ai](https://6000-firebase-studio-1753552635927.cluster-bg6uurscprhn6qxr6xwtrhvkf6.cloudworkstations.dev/)

---
## Impact

- 90% reduction in manual camera monitoring efforts.  
- Proactive threat detection increasing safety and saving lives.  
- Cost-effective cloud-based scalable analytics for thousands of camera feeds.  
- Supports multilingual voice commands and citizen interfaces (planned).  

---

## Future Work

- Integration of appearance-based re-identification models for robust multi-person tracking.  
- Enhanced drone autonomy with predictive zone risk evaluation.  
- Edge AI deployment for ultra-low latency detection.  
- Public integration for real-time incident reporting and crowd coordination.  

---

*Thank you for checking out Drishti-360! Together, let's make large public events safer with AI-driven insights.*  
