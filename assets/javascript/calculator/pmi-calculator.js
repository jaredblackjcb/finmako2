waitForElement('#pmi-data').then(() => {
    const pmiForm = document.querySelector('#pmi-calculator-form');
    pmiForm.scrollIntoView({behavior: "auto", block: "start", inline: "nearest"});
})

function waitForElement(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        }
        
        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}