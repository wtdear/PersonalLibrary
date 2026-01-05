import { useEffect } from 'react';

function PageIcon({ iconName }) {
    useEffect(() => {
        
        const favicon = document.querySelector("link[rel*='icon']");
        if (!favicon) {
            const newFavicon = document.createElement('link');
            newFavicon.rel = 'icon';
            newFavicon.type = 'image/png';
            newFavicon.href = `/favicon-${iconName}.png`;
            document.head.appendChild(newFavicon);
            return;
        }
        
        const newPath = `/favicon-${iconName}.png`;
        
        const testImage = new Image();
        testImage.onload = function() {
            favicon.href = newPath;
            favicon.type = 'image/png';
        };
        testImage.onerror = function() {
            console.error(`❌ Favicon file NOT FOUND: ${newPath}`);
            console.log('📁 Available files in public/ should be:');
            console.log('- favicon-library.png');
            console.log('- favicon-books.png');
            console.log('- favicon-films.png');
            console.log('- favicon-games.png');
        };
        testImage.src = newPath;
        
    }, [iconName]);
    
    return null;
}

export default PageIcon;