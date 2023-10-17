function setLastLanguage(lang)
{
    lang = lang.toLowerCase();
    if(typeof(Storage) !== 'undefined')
        localStorage.setItem('lastSelectedLanguage', lang);
}

function getLastLanguage()
{
    if(typeof(Storage) !== 'undefined')
    {
        const lang = localStorage.getItem('lastSelectedLanguage');
        if(lang)
            return lang;
    }
    return 'python';
}

document.querySelectorAll('.multi-language-switcher').forEach(multiLanguageSwitcher => {
    const tabsContent = document.createElement('div');
    tabsContent.className = 'tabs-content';

    while(multiLanguageSwitcher.firstChild) {
        tabsContent.appendChild(multiLanguageSwitcher.firstChild);
    }

    const tabsHeader = document.createElement('div');
    tabsHeader.className = 'tabs-header';

    multiLanguageSwitcher.insertBefore(tabsHeader, multiLanguageSwitcher.firstChild);

    multiLanguageSwitcher.appendChild(tabsContent);


    const codeElements = tabsContent.querySelectorAll('code.hljs');

    // collect langs:
    var languages = [];
    codeElements.forEach(function(codeElement) {
        const classNames = codeElement.className.split(' ');
        classNames.forEach(function(className) {
            if(className.startsWith('language-')) {
                var languageName = className.replace(/^language-/, '');
                languages.push(languageName);
            }
        });
    });
    console.log('Languages', languages);

    var lastLangIdx = Math.max(0, languages.indexOf(getLastLanguage()));

    var index = 0;
    codeElements.forEach(function(codeElement) {
        if(index != lastLangIdx) codeElement.style.display = 'none';

        const classNames = codeElement.className.split(' ');
        classNames.forEach(function(className) {
            if(className.startsWith('language-')) {
                var languageName = className.replace(/^language-/, '');
                languageName = languageName.charAt(0).toUpperCase() + languageName.slice(1).toLowerCase();

                const button = document.createElement('button');
                button.innerText = languageName;
                button.setAttribute('data-id', className);
                if(index == lastLangIdx) button.classList.add('active');
                button.addEventListener('click', e => {
                    setLastLanguage(languageName);
                    tabsHeader.querySelectorAll('button').forEach(e => e.classList.remove('active'));
                    button.classList.add('active');
                    tabsContent.querySelectorAll('code.hljs').forEach(e => e.style.display = 'none');
                    tabsContent.querySelectorAll('code.hljs.' + className).forEach(e => e.style.display = 'block');
                });
                tabsHeader.appendChild(button);
            }
        });

        index++;
    });
});
