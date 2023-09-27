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
    var first = true;
    codeElements.forEach(function(codeElement) {
        if(!first) codeElement.style.display = 'none';

        const classNames = codeElement.className.split(' ');
        classNames.forEach(function(className) {
            if(className.startsWith('language-')) {
                var languageName = className.replace(/^language-/, '');
                languageName = languageName.charAt(0).toUpperCase() + languageName.slice(1).toLowerCase();

                const button = document.createElement('button');
                button.innerText = languageName;
                button.setAttribute('data-id', className);
                if(first) button.classList.add('active');
                button.addEventListener('click', e => {
                    tabsHeader.querySelectorAll('button').forEach(e => e.classList.remove('active'));
                    button.classList.add('active');
                    tabsContent.querySelectorAll('code.hljs').forEach(e => e.style.display = 'none');
                    tabsContent.querySelectorAll('code.hljs.' + className).forEach(e => e.style.display = 'block');
                });
                tabsHeader.appendChild(button);
            }
        });

        first = false;
    });
});
