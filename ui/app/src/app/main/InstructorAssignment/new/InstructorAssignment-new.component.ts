import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'InstructorAssignment-new',
  templateUrl: './InstructorAssignment-new.component.html',
  styleUrls: ['./InstructorAssignment-new.component.scss']
})
export class InstructorAssignmentNewComponent {
  @ViewChild("InstructorAssignmentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}