function toggleSidebar() {
    const sidebar = 
        document.getElementById("sidebarContainer"); 
    const overlay = 
        document.getElementById("sidebarOverlay"); 
        sidebar.classList.toggle("active"); 
        overlay.classList.toggle("active"); 
    }