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

 describe('Exclusões', () => {
    it('Exclusão', () => {
    cy.visit('http://127.0.0.1:8000/lista/');
    cy.get(' Código: 123').click();
    cy.get('Deletar').click();
    cy.get('[type=Submit]').click();
    });
 });