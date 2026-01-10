import streamlit as st

OPTIONS = {
    "EC2": {
        "cost": 3, "scaling": 3, "ops": 2, "latency": 4,
        "pros": ["Full control", "Custom configuration"],
        "cons": ["Manual scaling", "Ops heavy"]
    },
    "Lambda": {
        "cost": 5, "scaling": 5, "ops": 5, "latency": 3,
        "pros": ["Serverless", "Auto scaling", "Low ops"],
        "cons": ["Cold starts", "Execution limits"]
    },
    "ECS": {
        "cost": 4, "scaling": 4, "ops": 3, "latency": 4,
        "pros": ["Containerized", "Better control"],
        "cons": ["More setup than Lambda"]
    }
}

st.title("⚖️ Cloud Referee")

a = st.selectbox("Select Option A", list(OPTIONS.keys()))
b = st.selectbox("Select Option B", list(OPTIONS.keys()), index=1)

st.subheader("Your priorities")
cost = st.slider("Cost sensitivity", 1, 5, 3)
scaling = st.slider("Scaling importance", 1, 5, 3)
ops = st.slider("Ops simplicity importance", 1, 5, 3)
latency = st.slider("Latency importance", 1, 5, 3)

def score(opt, w):
    return (
        OPTIONS[opt]["cost"] * w["cost"] +
        OPTIONS[opt]["scaling"] * w["scaling"] +
        OPTIONS[opt]["ops"] * w["ops"] +
        OPTIONS[opt]["latency"] * w["latency"]
    )

if st.button("Compare"):
    w = {"cost": cost, "scaling": scaling, "ops": ops, "latency": latency}

    sa = score(a, w)
    sb = score(b, w)

    st.header("Results")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(a)
        st.write("**Pros**")
        for p in OPTIONS[a]["pros"]:
            st.write("✔", p)
        st.write("**Cons**")
        for c in OPTIONS[a]["cons"]:
            st.write("❌", c)
        st.write("Score:", sa)

    with col2:
        st.subheader(b)
        st.write("**Pros**")
        for p in OPTIONS[b]["pros"]:
            st.write("✔", p)
        st.write("**Cons**")
        for c in OPTIONS[b]["cons"]:
            st.write("❌", c)
        st.write("Score:", sb)

    st.subheader("Trade-off Explanation")
    st.write(f"{a} gives you **{OPTIONS[a]['pros'][0]}** but at the cost of **{OPTIONS[a]['cons'][0]}**.")
    st.write(f"{b} gives you **{OPTIONS[b]['pros'][0]}** but at the cost of **{OPTIONS[b]['cons'][0]}**.")

    if sa > sb:
        st.success(f"✅ Recommended: {a}")
    elif sb > sa:
        st.success(f"✅ Recommended: {b}")
    else:
        st.info("⚖️ Both options score equally based on your priorities.")
