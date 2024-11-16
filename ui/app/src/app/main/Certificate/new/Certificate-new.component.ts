import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Certificate-new',
  templateUrl: './Certificate-new.component.html',
  styleUrls: ['./Certificate-new.component.scss']
})
export class CertificateNewComponent {
  @ViewChild("CertificateForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}