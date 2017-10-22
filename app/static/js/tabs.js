/*
JavaScript to handle tabs
@author nano-bytes and signare
*/

function chargeButtonsAndOpenDefault(){
    clickButtons();
    setTimeout(openDefaultTab, 100);
}

function openDefaultTab(){
    var defaultTab = $('#default-tab');
    defaultTab.click();
}

function clickButtons(){
    $('button').click(function(event){
        var tabName = event.target.getAttribute('data-tab');
        clearAttributes();
        openTab(tabName);
    });
}

function clearAttributes() {
    var i, tabContent, tabLink, activeTab;
    tabContent = $('.tab-content');
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = 'none';
        tabContent[i].className = 'tab-content';
    }
    tabLink = $('.tab-link');
    for (i = 0; i < tabLink.length; i++) {
          tabLink[i].className = '';
    }
}

function openTab(tabName){
    activeTab = document.getElementById(tabName);
    activeTab.style.display = 'block';
    activeTab.className += ' active';
}

$(window).load(chargeButtonsAndOpenDefault);