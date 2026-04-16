import { Component, signal } from '@angular/core';
import { AddItem } from './add-item/add-item';
@Component({
  selector: 'app-root',
  imports: [AddItem],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('angular-app');
}
