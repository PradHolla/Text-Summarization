import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"{st.secrets['api_token']}"}

st.set_page_config(page_title="Text Summarizer" ,layout="wide", page_icon=":books:")
st.header("Text Summarizer")
st.subheader("Summarize your text in a few clicks")

with st.sidebar:
    st.header("Summary Settings")
    st.subheader("Set the minimum and maximum no. of words of the summary")
    min_length = st.slider("Minimum Length", min_value=100, max_value=300, value=250)
    max_length = st.slider("Maximum Length", min_value=200, max_value=500, value=400)

expander = st.expander("Sample Text")
expander.write("Albert Einstein(14 March 1879 – 18 April 1955) was a German-born theoretical physicist, widely acknowledged to be one of the greatest and most influential physicists of all time. Einstein is best known for developing the theory of relativity, but he also made important contributions to the development of the theory of quantum mechanics. Relativity and quantum mechanics are together the two pillars of modern physics. His mass–energy equivalence formula E = mc2, which arises from relativity theory, has been dubbed \"the world's most famous equation\". His work is also known for its influence on the philosophy of science. He received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\", a pivotal step in the development of quantum theory. His intellectual achievements and originality resulted in \"Einstein\" becoming synonymous with \"genius\". In 1905, a year sometimes described as his annus mirabilis (\'miracle year\'), Einstein published four groundbreaking papers. These outlined the theory of the photoelectric effect, explained Brownian motion, introduced special relativity, and demonstrated mass-energy equivalence. Einstein thought that the laws of classical mechanics could no longer be reconciled with those of the electromagnetic field, which led him to develop his special theory of relativity. He then extended the theory to gravitational fields; he published a paper on general relativity in 1916, introducing his theory of gravitation. In 1917, he applied the general theory of relativity to model the structure of the universe.He continued to deal with problems of statistical mechanics and quantum theory, which led to his explanations of particle theory and the motion of molecules. He also investigated the thermal properties of light and the quantum theory of radiation, which laid the foundation of the photon theory of light.\
            \nHowever, for much of the later part of his career, he worked on two ultimately unsuccessful endeavors. First, despite his great contributions to quantum mechanics, he opposed what it evolved into, objecting that \"God does not play dice\". Second, he attempted to devise a unified field theory by generalizing his geometric theory of gravitation to include electromagnetism. As a result, he became increasingly isolated from the mainstream of modern physics.\
            \nEinstein was born in the German Empire, but moved to Switzerland in 1895, forsaking his German citizenship (as a subject of the Kingdom of Württemberg) the following year. In 1897, at the age of 17, he enrolled in the mathematics and physics teaching diploma program at the Swiss Federal polytechnic school in Zürich, graduating in 1900. In 1901, he acquired Swiss citizenship, which he kept for the rest of his life, and in 1903 he secured a permanent position at the Swiss Patent Office in Bern. In 1905, he was awarded a PhD by the University of Zurich. In 1914, Einstein moved to Berlin in order to join the Prussian Academy of Sciences and the Humboldt University of Berlin. In 1917, Einstein became director of the Kaiser Wilhelm Institute for Physics; he also became a German citizen again, this time Prussian.\
            \nIn 1933, while Einstein was visiting the United States, Adolf Hitler came to power in Germany. Einstein, as Jewish, objected to the policies of the newly elected Nazi government; he settled in the United States and became an American citizen in 1940. On the eve of World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential German nuclear weapons program and recommending that the US begin similar research. Einstein supported the Allies but generally denounced the idea of nuclear weapons.")

text = st.text_area("Enter Text Here", height=300)
summarize = st.button("Summarize")

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if text is not None and summarize:
    payload = {"inputs": text, "parameters": {"max_length": max_length, "min_length": min_length, "do_sample": False}}
    response = query(payload)
    summary = response[0]['summary_text']
    summary = summary.split('.')
    summary = list(filter(None, summary))
    for i in range(len(summary)):
        summary[i] = '- ' + summary[i] + '.'
    listToStr = '\n'.join([str(ele) for ele in summary])
    st.write(listToStr)