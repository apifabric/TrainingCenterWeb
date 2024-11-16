import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Enrollment-new',
  templateUrl: './Enrollment-new.component.html',
  styleUrls: ['./Enrollment-new.component.scss']
})
export class EnrollmentNewComponent {
  @ViewChild("EnrollmentForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}