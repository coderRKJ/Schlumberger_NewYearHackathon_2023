const temp_message = new Map();

chrome.runtime.onInstalled.addListener(() => {
    chrome.action.setBadgeText({
        text: "0",
    });
});
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.length) {
        temp_message.set(sender.tab.id, message);
        chrome.action.setBadgeText({
            tabId: sender.tab.id,
            text: `${message.length}`,
        });
    } else {
        const data = new FormData();
        const arr = [];
        for (const value of temp_message.values()) {
            arr.push(...value);
        }
        data.append("json", JSON.stringify(arr));

        fetch("http://127.0.0.1:5000/post_urls",
            {
                method: "POST",
                body: data
            })
            .then(function (res) { return res.json(); })
            .then(function (data) { sendResponse(data['action']); })
            .catch(function (error) { console.error(error);sendResponse("Fetch failed. Make sure server is running. See console for more info."); });
        
        for (const key of temp_message.keys()) {
            chrome.action.setBadgeText({
                tabId: key,
                text: "0",
            });
        }
        temp_message.clear();
        return true;
    }
})