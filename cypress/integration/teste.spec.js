/// <reference types="cypress" />

describe('Cadastros', () => {
    it('Cadastro', () => {
    cy.visit('http://127.0.0.1:8000/novo/');

    cy.get('[name=Codigo]').type('123');
    cy.get('[name=Preço]').type('40');
    cy.get('[name=Quantidade]').type('7');
    cy.get('[name=Data]').type('06/29/21');

    cy.get('[type=Submit]').click();
    });
 });

 describe('Listagens', () => {
    it('Listagem', () => {
    cy.visit('http://127.0.0.1:8000/');

    cy.get('main.container > :nth-child(2) > a')
     cy.intercept(
      {
        method: 'GET',
        url: '/lista'
        },{})
    });
 });

 describe('Exclusões', () => {
    it('Exclusão', () => {
    cy.visit('http://127.0.0.1:8000/lista/');
    cy.contains('Código: 123').click();
    cy.intercept(
      {
        method: 'DELETE',
        url: '/delete/**'
        },{})
    cy.get('main.container > a').click();
    cy.get('button').click();
    });
 });