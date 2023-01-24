console.log("WebCrawl is active.")

const header_text = document.getElementById("header");

header_text.addEventListener("click", ()=>{header_text.style.cursor="progress";chrome.runtime.sendMessage(message=[], (response) => {
    header_text.style.cursor="pointer";alert(response);
});})