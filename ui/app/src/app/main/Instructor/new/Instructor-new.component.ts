import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Instructor-new',
  templateUrl: './Instructor-new.component.html',
  styleUrls: ['./Instructor-new.component.scss']
})
export class InstructorNewComponent {
  @ViewChild("InstructorForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}