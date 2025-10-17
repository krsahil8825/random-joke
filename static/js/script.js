document.addEventListener("DOMContentLoaded", () => {
    formHandler();
    setupCopyButton();
});

function formHandler() {
    const getform = document.getElementById("jokeForm");
    getform.addEventListener("submit", (e) => {
        e.preventDefault();
        const jokeType = document.getElementById("joke-type").value;
        const resultSection = document.getElementById("resultSection");
        const randomJokeDisplay = document.getElementById("randomJokeDisplay");

        fetch(`/api/${jokeType}`, {
            method: "GET",
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.joke) {
                    randomJokeDisplay.textContent = data.joke;
                    resultSection.style.display = "block";
                } else {
                    randomJokeDisplay.textContent = "No joke found!";
                    resultSection.style.display = "block";
                }
            })
            .catch((error) => {
                console.error("Error fetching joke:", error);
                randomJokeDisplay.textContent = "Error fetching joke. Please try again.";
                resultSection.style.display = "block";
            });
    });
}

function setupCopyButton() {
    const copyBtn = document.getElementById("copyBtn");
    copyBtn.addEventListener("click", () => {
        const jokeText = document.getElementById("randomJokeDisplay").textContent;
        navigator.clipboard
            .writeText(jokeText)
            .then(() => {
                const originalText = copyBtn.textContent;
                const range = document.createRange();
                range.selectNode(document.getElementById("randomJokeDisplay"));
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);
                copyBtn.textContent = "Copied!";
                setTimeout(() => {
                    copyBtn.textContent = originalText;
                }, 2000);
            })
            .catch((error) => {
                console.error("Error copying joke:", error);
                copyBtn.textContent = "Failed to copy!";
            });
    });
}
