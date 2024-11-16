import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CourseMaterial-new',
  templateUrl: './CourseMaterial-new.component.html',
  styleUrls: ['./CourseMaterial-new.component.scss']
})
export class CourseMaterialNewComponent {
  @ViewChild("CourseMaterialForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}