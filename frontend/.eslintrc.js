// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
  // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
  extends: ['plugin:vue/essential', 'airbnb-base'],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // check if imports actually resolve
  settings: {
    'import/resolver': {
      webpack: {
        config: 'build/webpack.base.conf.js'
      }
    }
  },
  // add your custom rules here
  rules: {
    // don't require .vue extension when importing
    'import/extensions': ['error', 'always', {
      js: 'never',
      vue: 'never',
    }],
    'indent': 'off',
    'quotes': 'off',
    'arrow-parens': 'off',
    'no-trailing-spaces': 'off',
    'comma-dangle': 'off',
    'func-names': 'off',
    'prefer-arrow-callback': 'off',
    'max-len': 'off',
    'camelcase': 'off',
    'no-restricted-syntax': 'off',
    'guard-for-in': 'off',
    'no-param-reassign': 'off',
    'no-return-assign': 'off',
    'no-console': 'off',
    'no-undef': 'off',
    'dot-notation': 'off',
    'no-unused-vars': 'off',
    'no-underscore-dangle': 'off',
    'no-constant-condition': 'off',
    'import/no-extraneous-dependencies': ['error', {
      optionalDependencies: ['test/unit/index.js']
    }],
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off'
  }
}
