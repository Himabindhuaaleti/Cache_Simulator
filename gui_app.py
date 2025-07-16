import streamlit as st
from policies.fifo import FIFO_Cache
from policies.lru import LRU_Cache

def display_cache(stack, evicted=None):
    st.markdown("#### 📦 Cache Stack (Top → Bottom):")
    for i, page in enumerate(reversed(stack)):
        tag = " - ❌ Evicted" if evicted == page and i == 0 else ""
        st.write(f"🔹 {page}{tag}")
    st.markdown("---")

def simulate(policy_name, pages, capacity):
    cache = FIFO_Cache(capacity) if policy_name == "FIFO" else LRU_Cache(capacity)
    history = []
    for i, page in enumerate(pages, 1):
        prev_stack = list(cache.queue if policy_name == "FIFO" else cache.pages)
        new_stack, evicted, hit = cache.access(page)
        history.append({
            "step": i,
            "page": page,
            "hit": hit,
            "old_stack": prev_stack,
            "new_stack": new_stack,
            "evicted": evicted
        })
    return history, cache.get_stats()

st.title("🧠 Cache Simulator (LRU & FIFO)")
capacity = st.number_input("Enter Cache Size", min_value=1, value=3)
policy = st.radio("Choose Replacement Policy", ("LRU", "FIFO"))
page_input = st.text_input("Enter Page Reference String (e.g., 1 2 3 2 4 1)")

if st.button("Simulate"):
    try:
        pages = list(map(int, page_input.strip().split()))
        history, (hits, misses) = simulate(policy, pages, capacity)

        for h in history:
            st.markdown(f"### Step {h['step']}: Accessed Page {h['page']}")
            st.markdown("#### 🔍 Explanation:")
            if h['hit']:
                st.success("✅ HIT: Page is already in the cache.")
                if policy == "LRU":
                    st.info("LRU: Page moved to most recently used position.")
            else:
                st.error("❌ MISS: Page is not in the cache.")
                if h['evicted'] is not None:
                    st.warning(f"Cache is full. Evicted page: {h['evicted']}")
                else:
                    st.info("Added to cache. No eviction required.")

            st.markdown("**Before Access:**")
            display_cache(h["old_stack"], evicted=h["evicted"] if not h["hit"] else None)
            st.markdown("**After Access:**")
            display_cache(h["new_stack"])

        total = hits + misses
        st.markdown("## 📊 Final Report")
        st.write(f"**Total Requests**: {total}")
        st.write(f"**Hits**: {hits}")
        st.write(f"**Misses**: {misses}")
        st.write(f"**Hit Ratio**: {hits / total:.2f}")
    except Exception as e:
        st.error(f"❗ Error: {e}")