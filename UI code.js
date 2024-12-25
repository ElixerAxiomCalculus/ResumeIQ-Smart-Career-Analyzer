document.getElementById("upload").onsubmit = async (e) => {
    e.preventDefault();

    const File = document.getElementById("resume").files[0];
    if (!File) {
        alert("Select a file to upload");
        return;
    }

    const Data = new FormData();
    Data.append("File", File);

    // Show the loading spinner
    document.getElementById("loading").style.display = "block";
    document.getElementById("response").style.display = "none"; // Hide response section initially

    try {
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: 'POST',
            body: Data
        });

        const result = await response.json();

        // Hide the loading spinner once the response is received
        document.getElementById("loading").style.display = "none";

        if (response.ok) {
            // Display extracted text and predicted field in the UI
            document.getElementById("extractedText").value = result.extracted_text || "No extracted text available.";
            document.getElementById("predictedField").textContent = result.predicted_field || "No prediction available.";
            document.getElementById("response").style.display = "block"; // Show the results
        } else {
            document.getElementById("response").textContent = result.message || "Error in processing the file.";
            document.getElementById("response").style.display = "block"; // Show error message
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("loading").style.display = "none"; // Hide loading spinner
        document.getElementById("response").textContent = "Error in uploading the file.";
        document.getElementById("response").style.display = "block"; // Show error message
    }
};
