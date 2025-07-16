# 🧠 Cache Simulator (LRU & FIFO)

A Python-based interactive simulator to understand **cache replacement policies** — focusing on **LRU (Least Recently Used)** and **FIFO (First-In First-Out)**.

Designed to make these concepts **easy to visualize** using an intuitive **Streamlit GUI**. This project is aimed at students, educators, and anyone preparing for **Operating Systems, Systems Design, or DSA interviews**.

---

## 📽️ Demo

> 🎥 *(Add a screenshot or GIF here showing the app before/after a page request)*

---

## 🚀 Features

- ✅ Supports **LRU** and **FIFO** replacement strategies  
- 🔢 Accepts user-defined **cache size** and **page reference string**  
- 🎯 Shows **hit/miss result** for every access  
- 📦 Displays **cache state as a stack** before and after each operation  
- 🔍 Includes **explanations for each transition**  
- 📊 Final summary: hit count, miss count, and hit ratio  

---

## 📚 What I Learned

This project helped me:
- Simulate real-world cache behavior from **Operating System concepts**
- Understand **difference between LRU and FIFO**
- Design a user-friendly interface with **Streamlit**
- Strengthen **data structure implementation** using Python lists
- Practice **interview-style explanation** of algorithmic behavior

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** (for front-end GUI)
- Core data structures: Lists & Queues

---

## 📂 Folder Structure

```
cache_simulator/
│
├── gui_app.py              # Main GUI file
├── policies/
│   ├── fifo.py             # FIFO Cache Logic
│   └── lru.py              # LRU Cache Logic
```

---

## 💡 How to Run the Project

### 1. Clone the repo
```bash
git clone https://github.com/your-username/cache-simulator.git
cd cache-simulator
```

### 2. Install dependencies
```bash
pip install streamlit
```

### 3. Run the application
```bash
streamlit run gui_app.py
```

---

## 📈 Sample Output (Text Format)

```
Step 4: Accessed Page 2
❌ MISS: Page is not in the cache.
📦 Before Access: [1, 3]
📦 After Access:  [3, 1, 2]
Evicted: None
```

---

## 🔄 How It Works

### ✅ LRU (Least Recently Used)
- Pages are ordered by recency of use
- On **hit**, page moves to the **most recently used position**
- On **miss**, and if full, **least recently used page is evicted**

### ✅ FIFO (First-In First-Out)
- Pages are evicted in the order they entered the cache
- Oldest page is removed first on a **miss** if cache is full

---

## 🔍 Key Terminology

- **Cache**: A small memory space storing frequently accessed data.
- **Hit**: Requested data is already present in the cache.
- **Miss**: Requested data is not present — must fetch & insert it.
- **Eviction**: Removing a page to make room for new ones.

---

## 💼 Interview Questions & Point-Wise Answers

### ❓ 1. What is the difference between FIFO and LRU?

**FIFO (First-In First-Out):**
- Evicts the page that was inserted **first**, regardless of usage.
- Simple to implement using a **queue**.
- Doesn't consider how recently a page was used.

**LRU (Least Recently Used):**
- Evicts the page that was used **least recently**.
- Maintains usage order dynamically.
- Requires more logic (e.g., list updates or doubly linked list in real systems).

---

### ❓ 2. When is LRU better than FIFO?

- When **recency of access** matters.
- LRU reduces misses in workloads where recently used data is likely to be reused soon.
- Better suited for applications with **temporal locality** (e.g., web browsing, DB queries).

---

### ❓ 3. What data structures did you use to implement cache?

- **Python List**:
  - Acts like a stack or queue.
  - For LRU, we remove and append to reflect recency.
  - For FIFO, we `pop(0)` to evict the oldest element.
- Could optimize with **deque** or **OrderedDict** in larger apps.

---

### ❓ 4. How is a cache hit or miss detected?

- On every access:
  - Check if the page is **already in cache** → **Hit**
  - If not present → **Miss**
- Cache logic updates accordingly:
  - For LRU: move page to end.
  - For FIFO: append page, possibly evicting the oldest.

---

### ❓ 5. How is eviction handled?

- When cache is **full** and a **miss** occurs:
  - FIFO: Remove the **first inserted page**.
  - LRU: Remove the **least recently used page**.
- This ensures space is made for the new page.

---

### ❓ 6. Why did you use Streamlit?

- It allows for rapid prototyping of GUIs in Python.
- Highly readable and beginner-friendly.
- Suitable for educational and visual simulations.
- Can be deployed online easily for demo purposes.

---

### ❓ 7. What is the time complexity of your access function?

- **Lookup (Hit/Miss check):** O(n) for list
- **Eviction and insert:** O(n) worst case (list operations)
- For real-world systems, better performance is achieved with:
  - HashMaps + Doubly Linked List (for O(1) LRU)

---

## 📌 Future Improvements

- Add support for more policies like **LFU** or **MRU**
- Deploy the app on **Streamlit Cloud** for public access
- Accept **file input** for real-world simulations
- Add **charts or graphs** to visualize performance stats

---

## 🤝 Contributing

Contributions and suggestions are welcome!  
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👩‍💻 Author

**Bindhu Sweelty**  
Final Year Computer Science Undergraduate  
Passionate about DSA, Systems Programming, and Real-Time Applications  
[GitHub](https://github.com/) • [LinkedIn](https://linkedin.com/)
