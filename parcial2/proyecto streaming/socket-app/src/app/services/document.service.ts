import { Injectable } from '@angular/core';

import { Socket } from 'ngx-socket-io';

import { Document } from '../models/document';

@Injectable({
  providedIn: 'root'
})
export class DocumentService {
  currentDocument = this.socket.fromEvent<Document>('document');
  documents = this.socket.fromEvent<string[]>('documents');

  constructor(private socket: Socket) { }

  getDocument(id: string) {
    this.socket.emit('getDoc', id);
  }

  newDocument(docname: string) {
    this.socket.emit('addDoc', { id: docname, doc: '' });
  }

  editDocument(document: Document) {
    this.socket.emit('editDoc', document);
  }

  deleteDocument(id: string){
    this.socket.emit('deleteDoc', id);
    
  }
  
}
