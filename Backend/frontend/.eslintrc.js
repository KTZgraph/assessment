module.exports = {
    "parserOptions": {
        "ecmaVersion": 6,
        "sourceType": "module",
        "ecmaFeatures": {
            "jsx": true
        }
    },
    "rules": {
        'no-console': 'off',
    },
    "extends": ["vue", "standard", "plugin:vue/recommended"],
    "plugins": ["import", "vue"],
};