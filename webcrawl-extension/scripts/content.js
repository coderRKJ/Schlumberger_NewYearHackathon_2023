let feed_article_images = Array.from(document.getElementsByClassName("feeds-articles__image"))
let article_urls = feed_article_images.map(ele=>ele.href);
if (article_urls.length==0) {
    console.log("None Found");
}
else {
    chrome.runtime.sendMessage(message=article_urls);
}