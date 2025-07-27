import streamlit as st
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
from google.cloud import storage
import io
import base64

# Initialize Vertex AI SDK
vertexai.init(project="computervisionporject", location="us-central1")

VIDEO_PATH = "gs://sonali_test/agent_engine/output.mp4"

class VideoQAAgent:
    def __init__(self, video_path: str):
        self.video_path = video_path
        self.model = GenerativeModel("gemini-2.0-flash")
        
    def query(self, input: dict) -> dict:
        query_text = input.get("query")
        if not query_text:
            return {"output": "Error: 'query' key is required in input."}
            
        try:
            storage_client = storage.Client()
            bucket_name, blob_name = self.video_path.replace("gs://", "").split("/", 1)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            video_content = blob.download_as_bytes()
            
            video_part = Part.from_data(mime_type="video/mp4", data=video_content)
            text_part = Part.from_text(query_text)
            contents = [video_part, text_part]
            
            response = self.model.generate_content(contents)
            return {"output": response.text}
        except Exception as e:
            return {"output": f"Error processing query: {str(e)}"}

    def get_video_for_display(self):
        try:
            storage_client = storage.Client()
            bucket_name, blob_name = self.video_path.replace("gs://", "").split("/", 1)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            video_content = blob.download_as_bytes()
            return video_content
        except Exception as e:
            st.error(f"Error loading video for display: {str(e)}")
            return None

def main():
    st.set_page_config(page_title="Project Drishti", layout="wide")
    
    st.title("Project Drishti - 360")
    
    # Initialize session state
    if "agent" not in st.session_state:
        st.session_state.agent = VideoQAAgent(video_path=VIDEO_PATH)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Create two columns layout
    col1, col2 = st.columns([1, 1])
    
    # Left column - Video display
    with col1:
        st.subheader("Video")
        video_content = st.session_state.agent.get_video_for_display()
        if video_content:
            st.video(video_content)
        else:
            st.error("Unable to load video")
    
    # Right column - Chat interface
    with col2:
        st.subheader("Vertex AI Assistant")
        
        # Chat container with fixed height
        chat_container = st.container(height=500)
        
        # Display chat history
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.markdown(message["content"])
                else:
                    with st.chat_message("assistant", avatar="🤖"):
                        st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("What would you like to know about the video?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get agent response
            with st.spinner("Analyzing video..."):
                response = st.session_state.agent.query({"query": prompt})
                assistant_response = response["output"]
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            st.rerun()
        
        # Clear chat button
        if st.session_state.messages:
            if st.button("Clear Chat", key="clear_chat"):
                st.session_state.messages = []
                st.rerun()

if __name__ == "__main__":
    main()