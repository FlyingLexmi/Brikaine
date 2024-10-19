const mineflayer = require('mineflayer');
const { pathfinder, Movements, goals } = require('mineflayer-pathfinder');
const { GoalNear } = goals;
const { bot } = require("./config/serverOptions");

bot.once('spawn', () => {
    bot.loadPlugin(pathfinder);
    console.log(`[Brikaine] ready!`);
});


bot.on('chat', (sender, message) => {
    
});
