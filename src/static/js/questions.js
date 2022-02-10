document.addEventListener("DOMContentLoaded", () => {
    let activeTab;
    let tabsArr = Array.from(document.querySelectorAll(".idea-tab"));
    let iframe = document.querySelector(".idea-iframe");

    tabsArr.map((tab) => {
        tab.addEventListener('click', () => {
            setActiveTab(tab)
        })
    });
    function setActiveTab(element) {
        if (activeTab) activeTab.classList.remove("idea-tab-active");
        activeTab = element;
        activeTab.classList.add("idea-tab-active");
        iframe.src = activeTab.nextElementSibling.src;
    }
});