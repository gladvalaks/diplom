<script setup lang="ts">
import AsidePanel from './AsidePanel.vue';
</script>

<template>
    <div class="base-page">
        <AsidePanel class="base-page__aside-panel" />

        <div class="base-page__content">
            <RouterView></RouterView>
        </div>
    </div>
</template>
<style>
.base-page {
    display: flex;
    gap: 25px;
    height: 100%;
    padding-top: 150px;
    box-sizing: border-box;
    background-color: black;
    .base-page__aside-panel {
        width: 280px;
    }
    .base-page__content {
        flex-grow: 1;
    }
}

.entity-page {
    height: 100%;
    padding: 25px;
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 30px;
    border-top-left-radius: 20px;
    overflow: hidden;
    background-color: white;
    
    .entity-page__title {
        font-size: 48px;
        font-weight: 600;
    }
} 
</style>