# School Access POC with Graphs

This project is a POC that shows how graphs can be used to evaluate students' accessibility to school after street blockages caused by heavy rain and flooding.
## 📖 Introduction

After heavy rain, many streets in the neighborhood were flooded and impassable. This POC models the neighborhood as a graph, where:

- **Nodes** represent students' homes (Júlia, Antônio, Rafaela) and the school.  
- **Edges** represent the streets connecting those points.  

Flood blockages are simulated by removing edges, and we then evaluate whether each student can still reach the school within the same graph (neighborhoods without leaving its boundaries).

---

## 🎯 Goal

- Represent the neighborhood as a graph using the **NetworkX** library.  
- Simulate flooding by removing edges.  
- Check the connectivity (number of paths) between each home and the school, before and after the blockages.

---

## 📷 Visual representation of the graph

![image](https://github.com/user-attachments/assets/eec8d939-242a-41c5-9472-92704dd7064e)

---

## 🛠️ Tools and Technologies

- **Python 3.7+**  
- **NetworkX** (for graph modeling and analysis)   ( https://networkx.org/documentation/stable/tutorial.html )

---

## 📦 Project Structure

/
├── school_accessibility.py # Main script that builds the graph and runs the analyses
├── requirements.txt # Project dependencies
└── README.md # This file


---

## ⚙️ Installation and Usage

1. Clone this repository:  
   ```bash
   git clone https://github.com/pedroscarelli/school-accessibility-graphs.git
   cd school-accessibility-graphs
    ```
2. Create a virtual environment and install the dependencies:  
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```  
3. Run the script to see the results:  
```bash
    python school_accessibility.py
```  
## 📊 Results
Initial Connectivity (before the blockages)

    Júlia → School: 2 paths

    Rafaela → School: 2 paths

    Antônio → School: 1 path

## Connectivity After Blockages (flooded streets removed)

    Júlia → School: 1 path

    Rafaela → School: 1 path

    Antônio → School: 0 paths (access cut off)

## ⚠️ Challenges

    Graph Modeling
    Translating a real-world scenario (streets, flooding) into nodes and edges takes care to keep the representation faithful.

    Performance on Dense Graphs
    On graphs with many connections, connectivity analysis can get slow, especially when recalculating paths after each edge removal.

## 📝 Conclusion

This POC shows that graphs are an effective tool for simulating and evaluating accessibility in disaster scenarios (flooding). Using NetworkX, we can quickly identify which students lost access to the school and how many alternative paths remain available.
