module.exports = {
  env: {
    node: true,
  },
  extends: 'airbnb-base',
  parserOptions: {
    sourceType: 'script',
    ecmaVersion: 2022,
  },
  globals: {
    window: true,
    document: true,
  },
  rules: {
    'max-len': 0,
    'arrow-parens': 0,
    'no-console': 0,
    'no-await-in-loop': 0,
    'object-curly-newline': 0,
    'no-promise-executor-return': 0,
    strict: 0,
    'no-multiple-empty-lines': ['error', { max: 2, maxBOF: 0, maxEOF: 0 }],
    'no-restricted-syntax': [
      'error',
      {
        selector: 'ForInStatement',
        message: 'for..in loops iterate over the entire prototype chain, which is virtually never what you want. Use Object.{keys,values,entries}, and iterate over the resulting array.',
      },
      {
        selector: 'LabeledStatement',
        message: 'Labels are a form of GOTO; using them makes code confusing and hard to maintain and understand.',
      },
      {
        selector: 'WithStatement',
        message: '`with` is disallowed in strict mode because it makes code impossible to predict and optimize.',
      },
    ],
  },
};
