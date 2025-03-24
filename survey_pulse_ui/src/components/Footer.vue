
<script setup lang="ts">
    const currentYear = (new Date()).getFullYear();
</script>
<template>  
    <footer class="bg-gray-800 text-white py-4">
        <div class="container mx-auto text-center">
            <p>&copy; {{ currentYear }} Survey Pulse. All rights reserved.</p>
            <div class="mt-2">
                <a href="#" class="text-gray-400 hover:text-white mx-2">Privacy Policy</a>
                <a href="#" class="text-gray-400 hover:text-white mx-2">Terms of Service</a>
                <a href="#" class="text-gray-400 hover:text-white mx-2">Contact Us</a>
            </div>
        </div>
    </footer>
</template>