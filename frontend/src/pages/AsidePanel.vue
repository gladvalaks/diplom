<script setup lang="ts">
</script>
<template>
    <div class="aside-panel">
        <div class="aside-panel__card">
            <RouterLink :to="{name: 'constructions'}">Объекты</RouterLink>
        </div>
        <div class="aside-panel__card">
            <RouterLink :to="{name: 'clients'}">Клиенты</RouterLink>
        </div>
        <div class="aside-panel__card">
            <RouterLink :to="{name: 'constructions-types-page'}">Типы объектов</RouterLink>
        </div>
        <div class="aside-panel__card">
            <RouterLink :to="{name: 'contractors-page'}">Подрядчики</RouterLink>
        </div>
    </div>
</template>
<style >
.aside-panel {
    display: flex;
    flex-direction: column;
    gap: 25px;

    .aside-panel__card {
        background-color: yellow;
        height: 50px;
        padding-left: 15px;
        border-bottom-right-radius: 10px;
        border-top-right-radius: 10px;
        a {
            color: black;
            font-size: 28px;
            line-height: 36px;
            text-decoration: none;
        }
        a:hover {
            color: red;
        }
    }
}
</style>