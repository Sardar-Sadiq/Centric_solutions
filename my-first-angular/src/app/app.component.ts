import { Component, signal } from '@angular/core';

import { CoursesComponent } from './courses.component';

@Component({
  selector: 'app-root',
  // imports: [CoursesComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('Angular app');
}
